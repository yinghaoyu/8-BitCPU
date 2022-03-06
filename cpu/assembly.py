# coding=utf-8

import pin

# 取指令,共3个字节,第1字节为操作码,第2字节为目的操作数,第3字节为源操作数
# 取指令总共需要6个微指令周期
FETCH = [
        pin.PC_OUT | pin.MAR_IN, # 把PC的数据输出到BUS,再从BUS读到MAR,PC作为RAM的基地址
        pin.RAM_OUT | pin.IR_IN | pin.PC_INC, # 把RAM[PC]的数据读出到BUS,再从BUS读到IR,PC自增1
        pin.PC_OUT | pin.MAR_IN,
        pin.RAM_OUT | pin.DST_IN | pin.PC_INC,
        pin.PC_OUT | pin.MAR_IN,
        pin.RAM_OUT | pin.SRC_IN | pin.PC_INC,
        ]

MOV = 0 | pin.ADDR2 # 0b1000_0000

ADD = (1 << pin.ADDR2_SHIFT) | pin.ADDR2 # 0b1001_0000

NOP = 0 # 0b0000_0000
HLT = 0x3f # 0b0111_1111

INSTRUCTIONS = {
    2: {
        MOV: {
            (pin.AM_REG, pin.AM_INS): [   # 立即数寻址
                pin.DST_W | pin.SRC_OUT,
            ],
            (pin.AM_REG, pin.AM_REG): [   # 寄存器寻址
                pin.DST_W | pin.SRC_R,    # 读出SRC的值送入DST
            ],
            (pin.AM_REG, pin.AM_DIR): [   # 直接寻址
                pin.SRC_OUT | pin.MAR_IN, # 先将SRC的值送入MAR,这是地址
                pin.DST_W | pin.RAM_OUT   # 取出RAM[SRC]的值送入DST
            ],
            (pin.AM_REG, pin.AM_RAM): [   # 寄存器间接寻址
                pin.SRC_R | pin.MAR_IN,   # 
                pin.DST_W | pin.RAM_OUT
            ],
            (pin.AM_DIR, pin.AM_INS): [
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_OUT
            ],
            (pin.AM_DIR, pin.AM_REG): [
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_R,
            ],
            (pin.AM_DIR, pin.AM_DIR): [
                pin.SRC_OUT | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],
            (pin.AM_DIR, pin.AM_RAM): [
                pin.SRC_R | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_OUT | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],

            (pin.AM_RAM, pin.AM_INS): [
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_OUT
            ],
            (pin.AM_RAM, pin.AM_REG): [
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.SRC_R,
            ],
            (pin.AM_RAM, pin.AM_DIR): [
                pin.SRC_OUT | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ],
            (pin.AM_RAM, pin.AM_RAM): [
                pin.SRC_R | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_R | pin.MAR_IN,
                pin.RAM_IN | pin.T1_OUT,
            ]
        }
    },
    1: {},
    0: {
        NOP: [
            pin.CYC,
        ],
        HLT: [
            pin.HLT,
        ]
    }
}
