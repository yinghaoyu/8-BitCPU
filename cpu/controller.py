#coding=utf-8

import os
import pin
import assembly as ASM

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'micro.bin') # 将生成的文件导入ROM中

micro = [pin.HLT for _ in range(0x10000)] # 数组长2^16, 初始化全填HLT

def compile_addr2(addr, ir, psw, index):
    global micro

    op = ir & 0xf0
    amd = (ir >> 2) & 3
    ams = ir & 3
    
    INST = ASM.INSTRUCTIONS[2]

    if op not in INST:
        micro[addr] = pin.CYC
        return
    am = (amd, ams)
    if am not in INST[op]:
        micro[addr] = pin.CYC
        return

    EXEC = INST[op][am]
    if index < len(EXEC):
        micro[addr] = EXEC[index]
    else:
        micro[addr] = pin.CYC

def compile_addr1(addr, ir, psw, index):
    pass

def compile_addr0(addr, ir, psw, index):
    global micro
    op = ir
    
    INST = ASM.INSTRUCTIONS[0]

    if op not in INST:
        micro[addr] = pin.CYC
        return

    EXEC = INST[op]
    if index < len(EXEC):
        micro[addr] = EXEC[index]
    else:
        micro[addr] = pin.CYC

for addr in range(0x10000):
    ir = addr >> 8 # 8~15位是指令码
    psw = (addr >> 4) & 0xf # 4~7位是程序状态字
    cyc = addr & 0xf # 0~3位是指令周期

    if cyc < len(ASM.FETCH): # 表示在指令周期内
        micro[addr] = ASM.FETCH[cyc] # 填充
        continue

    addr2 = ir & (1 << 7)
    addr1 = ir & (1 << 6)

    index = cyc - len(ASM.FETCH)

    if addr2:
        compile_addr2(addr, ir, psw, index)
    elif addr1:
        compile_addr1(addr, ir, psw, index)
    else:
        compile_addr0(addr, ir, psw, index)

with open(filename, 'wb') as file:
    for var in micro:
        value = var.to_bytes(4, byteorder='little') # 按小端写入
        file.write(value)

print('Compile micro instruction finish!')
