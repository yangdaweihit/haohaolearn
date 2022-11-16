## 删除所有变量
rm(list=ls())
## xlsx: 引入电子表格
## plyr: 批量处理data.frame
## rootSolve：求解方程
## ggplot2：画图
## latex2exp：在图中使用latex字符
require(openxlsx)
require(purrr)
require(plyr)
require(gtools)
require(rootSolve)
require(ggplot2)
require(latex2exp)


## -----------------------------------------------------------
## 拉索模型控制数
## -----------------------------------------------------------

## isfem <- TRUE  ##对于已经进行过频率计算的情况，无需重新计算
isfem <- FALSE

## 设置索力范围(kN)和索长范围(m)
T.min <- 50;  T.max <- 350;  T.incr <- 50
L.min <- 10;  L.max <- 100;  L.incr <- 5

## 材料弹模(Pa)和半径(mm)、密度(kg/m3)
E <- 2.0e11; R <- 15.88; rho <- 7813.4

## 频阶
nfreq <- 10

## 弹簧刚度
## 左端：k1为横向支撑刚度，k2为旋转刚度
## 右端：k3为横向支撑刚度，k4为旋转刚度
k1 <- 1e10; k2 <- 1e10; k3 <- 1e10; k4 <- 1e10

## 有限元模拟，得到data和freq.data
## freq.data: f.1 f.2 ... (Hz)
## femata:   L(m)  T(1/1e5 N) m(kg/m) EI(Nm2) f.1 f.2 ....(Hz)

if(isfem){
    source("fem.R")
    write.table(tdata,file="data.txt",sep=",",row.names=FALSE)
} else {
    tdata <- read.table(file="data.txt",header=TRUE,sep=",")
}

## ## 取出最长、最短索的最大、最小拉力下的数据
## samples <- subset(x=tdata,L==min(tdata$L)|L==max(tdata$L))
## samples <- subset(x=samples,T==min(tdata$T)|T==max(tdata$T))
samples  <-  tdata 

##计算zeta2，并将列加入到samples中
samples <- transform(samples,zeta2 =T*1e5/2.0/EI )

## 计算gama4n
gama4fn <- function(m,EI,fn) { m*(2.0*pi*fn)^2/EI }

## 取出f开头的列的指标
index <- grep("^f.",colnames(samples))

## 取出相应列的名字
freqcol <- colnames(samples)[index]

## 取出名字中的数字，即明确各列频率对应的频阶
## 工程实践中，频阶未必连续
## 将非数字开头的内容都替换为空
freqn <- as.numeric(gsub('[^[:digit:]]+',"",freqcol))

## ## 计算各阶频率对应的gama
gama4 <- apply(samples[,index],2,gama4fn,m=samples$m,EI=samples$EI)

colnames(gama4) <- paste("gama",freqn,sep=".")
samples <- cbind(samples,gama4)

delta <- function(gama4,zeta2,L){
    sqrt( sqrt( gama4 + zeta2^2 ) - zeta2 ) * L
}

## 计算 delta.n 
index <- grep("^gama.",colnames(samples))
deltan <- apply(samples[,index],2,delta,zeta=samples$zeta2,L=samples$L)
colnames(deltan) <- paste("dlt",freqn,sep=".")
deltan <- as.data.frame(deltan)

## ## ---------------------------------------------------------------------
## ## 等效长度 
## ## ---------------------------------------------------------------------
## lenfun <- function(deltan,freq_order){
##     log(1.0 - freq_order*pi/deltan)
## }

## lnlen <- as.data.frame(map2(deltan,freqn,lenfun))
## colnames(lnlen) <- paste("lnlen",1:nfreq,sep=".")

## ##  ----------------------------------------------------------------------
## ## samples[,tail(names(samples),5)]  ## 最后5列
## ## coll <- tail(names(samples),5)
## ## samples <- samples[,!names(samples) %in% coll, drop=F]  ##删去某些利
## ## ----------------------------------------------------------------------

## ## ----------------------------------------------------------------------
## ## 拟合模型并校验
## ## 回归模型求得各阶系数a,b,c
## lmfun <- function(y) lm(y ~ L + T, data = samples)
## mdl <- lapply(lnlen,lmfun)

## ## 预测lenln，并计算有效长度len
## ## 这里仅为数值模拟时的参考，在实际索力测量中并无意义
## ## 因为实际测量，并不知道实际索力

## ## 索力方程，此处索力T单位取为牛顿N
## ## T 索力; l 索长(m); fn 频率(Hz); mm 线密度(kg/m)
## ## EI 刚度(Nmm2); mdln 模型
## eqnt <- function(T,para)
## {
##     l = para[1]
##     fn = para[2]
##     m = para[3] 
##     EI= para[4] 
##     norder = para[5] 
##     coff <- getcoff(mdl,norder)
##     a <- coff[3]
##     b <- coff[2] 
##     c <- coff[1] 
##     l.en <- ( 1.0 - exp( a*T/1.0e5 + b*l + c )) * l
##     w.n <- 2.0 * pi * fn
##     item1 <- m*w.n^2*l.en^2/(norder*pi)^2
##     item2 <- EI*(norder*pi)^2/(l.en)^2
##     res <- T - item1 + item2
## }

## getcoff <- function(mdl,n) mdl[[n]]$coefficient 
## solve <- function(para){
##     uniroot.all(eqnt,interval=c(0.2e5,4.0e5),lower=0.2e5,upper=4.0e5,
##                 para=para)
## }

## ## 取出f开头的列
## index <- grep("^f.",colnames(data))
## freqcol <- colnames(samples)[index]

## for (strfi in freqcol ){
##      norder <- as.numeric(gsub('[^[:digit:]]+',"",strfi))
##      T.pred <- apply(X=data.frame(tdata$L,tdata[strfi],tdata$m,tdata$EI,norder),MARGIN = 1,FUN=solve)
##      data <- cbind(tdata,T.pred)
##      colnames(tdata)[ncol(tdata)] <- paste("T",norder,sep=".")
## }

## ## 标注kesi
## data <- transform(tdata,kesi=sqrt(T*1e5/EI)*L)
## write.xlsx(tdata,file="data.xlsx")
