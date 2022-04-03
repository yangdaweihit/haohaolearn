## -----------------------------------------------------------
## 有限元模型
## -----------------------------------------------------------

## 面积(m2)、惯矩(m4)、线密度(kg/m)、刚度(Nm2)
A <- pi * (R/1000)^2; I <- pi * (R/1000)^4/4; m <-  rho*A
EI <- E*I

## 索力和索长向量，注意：索力单位由千牛转为牛顿(N)
T <- seq(from=T.min,to=T.max,by=T.incr)*1000
L <- seq(from=L.min,to=L.max,by=L.incr)

## 由T和L生成数据网格，构成模拟工况
lc <- expand.grid(T,L)
colnames(lc)[1] <- "T"
colnames(lc)[2] <- "L"

## 三段模型各段参数：半径、分段数、分段长度
## 0表示中段，1表示左段，2表示右段
r0 <- R;       r1 <- R;      r2 <- R
div0  <- 10;   div1  <- 1;   div2  <- 1
end1l <- 0.2;  end2l <- 0.2; end0l <- lc$L - end1l - end2l

fem.data <- cbind(k1=k1,k2=k2,k3=k3,k4=k4,
              mod=E,rho=rho,nfreq=nfreq,lc[1]) 
fem.data <- cbind(cable.end1.radius=r1,
              cable.end1.length=end1l,
              cable.end1.div=div1,
              cable.main.radius=r0,
              cable.main.length=end0l,
              cable.main.div=div0,
              cable.end2.raidus=r2,
              cable.end2.length=end2l,
              cable.end2.div2=div2,
              fem.data)

## 生成数据文件"data.txt"
write.table(fem.data,file="predata.txt",sep=",",row.names=FALSE,col.names=FALSE)

## 调用ansys，生成频率结果文件
system("ansys190 -b < v004.dat > v004.out")

## 从"freq_*"文件中收集频率
all.files <- list.files(full.names = T,pattern="freq_")

## 数据文件名字排序
all.files <- mixedsort(all.files)  

## 逐一读取文件得到频率list
freq.list <- lapply(all.files,function(i) read.table(i))

## 将所有频率list并列起来后转轶，每排由低阶到高阶排列
freq.data <- t(do.call(cbind,freq.list))

## 指定每列名称为"f.xx"，xx为频阶数
colnames(freq.data) <- paste("f",seq(1,nfreq),sep=".")

## 定义行名为自然数
rownames(freq.data) <- 1:nrow(freq.data)

## 将freq.data由list转化为data.frame
freq.data <- as.data.frame(freq.data)

## 删除临时文件，保持工作目录整洁
system("rm -rf file.* *.parm v004.out *.DAT freq_*")

## 合成数据
tdata <- cbind(L=lc$L,T=lc$T/1e5,m=m,EI=EI,freq.data)
