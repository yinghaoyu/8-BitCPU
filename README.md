# 8位CPU的设计与实现

## 指令系统

* 地址长度`16`位
* 指令`8`位、程序状态字`4`位、微程序周期`4`位

---

* 立即寻址
  * `MOV A, 5`
* 直接寻址
  * `MOV A, [5]`
* 寄存器寻址
  * `MOV A, B`
* 寄存器间接寻址
  * `MOV A, [B]`

---

* 二地址指令
  * `1xxx[aa][bb]`
* 一地址指令
  * `01xxxx[aa]`
* 零地址指令
  * `00xxxxxxxxxx`

## 调试环境

* logiccircuit 2.22.12
* python 3.10.2

## 说明

尊重开源社区创作者，此项目非原创，只是根据个人理解进行了复现，致谢原地址[@StevenBaby](https://github.com/StevenBaby/computer)
