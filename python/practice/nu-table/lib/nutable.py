#! /usr/bin/python3
# -*- coding: utf-8 -*-

#
# 圆形截面钢筋混凝土偏心受压构件正截面相对抗压承载力n_u表格
#
# nu(re, rho)
# 由 \eta e_0 / r 和 \rho f_sd / f_cd 插值 n_u
#
# rho(re, nuval)
# 由 \eta e_0 / r 和  n_u 反向推测 \rho f_sd / f_cd
#

import numpy as np
from scipy import interpolate
import bisect
import os


def nu(re, rho):
    """
    由相对偏心距re和折算配筋率rho查找nu
    """
    curpath = os.path.dirname(__file__)
    nutbl = np.genfromtxt(curpath + "/nu.csv", delimiter=",")
    # 横轴: \rho f_sd / f_cd
    tblx = nutbl[0, 1:]
    # 纵轴：\eta e0 / r
    tbly = nutbl[1:, 0]
    # n_u 数值
    tblz = nutbl[1:, 1:]
    tbl = interpolate.interp2d(tblx, tbly, tblz, kind='linear')

    res = tbl(re, rho)
    return res


def rho(re, nuval):
    """
    由于相对偏心距re和承载力系数nu查找折算配筋率rho
    """
    curpath = os.path.dirname(__file__)
    nutbl = np.genfromtxt(curpath + "/nu.csv", delimiter=",")
    # 横轴: \rho f_sd / f_cd
    tblx = nutbl[0, 1:]
    # 纵轴：\eta \e0 / r
    tbly = nutbl[1:, 0]

    # 由re查找所在区间, idy为区间序号
    # 若为0或大于序列长度，则表示re超出范围
    idy = bisect.bisect_left(tbly, re)


    if idy < 1 or idy > len(tbly):
        res = -1
        return res

    re1 = tbly[idy-1]
    re2 = tbly[idy]

    # 找出idy和idy+1两行nu值
    nux1 = nutbl[idy, 1:]
    nux2 = nutbl[idy + 1, 1:]

    # 在两行nu中插值出对应re的nu行
    nui = np.array([])
    for nu1, nu2 in zip(nux1, nux2):
        interf = interpolate.interp1d([re1, re2], [nu1, nu2], kind='linear')
        nui = np.append(nui, interf(re))

    # 由nuval找到nui序列中的区间
    idx = bisect.bisect_left(nui, nuval)

    if idx < 1:
        res = -1
        return res

    interf = interpolate.interp1d([nui[idx - 1], nui[idx]],
                                  [tblx[idx - 1], tblx[idx]],
                                  kind='linear')

    res = interf(nuval)
    res = float(np.format_float_positional(res, 3))
    return res

