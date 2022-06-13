# A tiny 8-bit CPU

## Instruction

* Total length `16` bit
* operator hold `8`bit
* eflags hold `4`bit
* microinstruction cycle hold `4` bit

---

* Address immediately
  * `MOV A, 5`
* Address directly
  * `MOV A, [5]`
* Address by register
  * `MOV A, B`
* Address by register indirectly
  * `MOV A, [B]`

---

* double-address instruction
  * `1xxx[aa][bb]`
* single-address instruction
  * `01xxxx[aa]`
* zero-address instruction
  * `00xxxxxx`

## For debug

* logiccircuit 2.22.12
* python 3.10.2

## Reference

Thanks to[@StevenBaby](https://github.com/StevenBaby/computer)
