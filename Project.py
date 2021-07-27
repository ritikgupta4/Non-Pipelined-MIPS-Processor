from collections import OrderedDict

data_mem = OrderedDict()
data_mem={                          #handling data
    0x00000000: "0x00000000",
    0x00000004: "0x00000000",
    0x00000008: "0x00000000",
    0x0000000c: "0x00000000",
    0x00000010: "0x00000000",
    0x00000014: "0x00000000",
    0x00000018: "0x00000000",
    0x0000001c: "0x00000000",
    0x00000020: "0x00000000",
    0x00000024: "0x00000000",
    0x00000028: "0x00000000",
    0x0000002c: "0x00000000",
    0x00000030: "0x00000000",
    0x00000034: "0x00000000",
    0x00000038: "0x00000000",
    0x0000003c: "0x00000000",
    0x00000040: "0x00000000",
    0x00000044: "0x00000000",
    0x00000048: "0x00000000",
    0x0000004c: "0x00000000",
    0x00000050: "0x00000000",
    0x00000054: "0x00000000",
    0x00000058: "0x00000000",
    0x0000005c: "0x00000000",
    0x00000060: "0x00000000",
    0x00000064: "0x00000000",
    0x00000068: "0x00000000",
    0x0000006c: "0x00000000",
    0x00000070: "0x00000000",
    0x00000074: "0x00000000",
    0x00000078: "0x00000000",
    0x0000007c: "0x00000000",
    0x00000080: "0x00000000"
}
# instruction_mem = OrderedDict()
# instruction_mem={
#     0x10100000: "0x00000000",
#     0x10100004: "0x00000000",
#     0x10100008: "0x00000000",
#     0x1010000c: "0x00000000",
#     0x10100010: "0x00000000",
#     0x10100014: "0x00000000",
#     0x10100018: "0x00000000",
#     0x1010001c: "0x00000000",
#     0x10100020: "0x00000000",
#     0x10100024: "0x00000000",
#     0x10100028: "0x00000000",
#     0x1010002c: "0x00000000",
#     0x10100030: "0x00000000",
#     0x10100034: "0x00000000",
#     0x10100038: "0x00000000",
#     0x1010003c: "0x00000000",
#     0x10100040: "0x00000000",
#     0x10100044: "0x00000000",
#     0x10100048: "0x00000000",
#     0x1010004c: "0x00000000",
#     0x10100050: "0x00000000",
#     0x10100054: "0x00000000",
#     0x10100058: "0x00000000",
#     0x1010005c: "0x00000000",
#     0x10100060: "0x00000000",
#     0x10100064: "0x00000000",
#     0x10100068: "0x00000000",
#     0x1010006c: "0x00000000",
#     0x10100070: "0x00000000",
#     0x10100074: "0x00000000",
#     0x10100078: "0x00000000",
#     0x1010007c: "0x00000000"
# }   
#input instructions for MIPS
regmem = OrderedDict()
regmem={          
    '00000':0,
    '01000':0,
    '01001':0,
    '01010':0,
    '01011':0,
    '01100':0,
    '01101':0,
    '01110':0,
    '01111':0,
    '10000':0,
    '10001':0,
    '10010':0,
    '10011':0,
    '10100':0,
    '10101':0,
    '10110':0,
    '10111':0,
    '11000':0,
    '11001':0
}
regmem_name={          
    '00000':'$zero',
    '01000':'$t0',
    '01001':'$t1',
    '01010':'$t2',
    '01011':'$t3',
    '01100':'$t4',
    '01101':'$t5',
    '01110':'$t6',
    '01111':'$t7',
    '10000':'$s0',
    '10001':'$s1',
    '10010':'$s2',
    '10011':'$s3',
    '10100':'$s4',
    '10101':'$s5',
    '10110':'$s6',
    '10111':'$s7',
    '11000':'$t8',
    '11001':'$t9'
}

instruction_mem = OrderedDict()
op=''
rs=''
rt=''
rd=''
shamt=''
fn=''
address=''
jump=''
btarget=''
cycle_count=0
pc=0x00400000

def add(rs,rt,rd):
    print(str(regmem[rs]) + "+" + str(regmem[rt]))
    print(str(regmem_name[rs]) + "+" + str(regmem_name[rt]))
    print()
    regmem[rd]=regmem[rs]+regmem[rt]

def addi(rs,rt,address):
    print(str(regmem[rs]) + "+" + str(int(address, 2)))
    print(str(regmem_name[rs]) + "+" + str(int(address, 2)))
    print()
    regmem[rt]=regmem[rs]+int(address,2)

def sub(rs,rt,rd):
    print(str(regmem[rs]) + "-" + str(regmem[rt]))
    print(str(regmem_name[rs]) + "-" + str(regmem_name[rt]))
    print()
    regmem[rd]=regmem[rs]-regmem[rt] 

def loadword(rs,rt,address):
    #print("loadword")
    if((regmem[rs]+int(address,2))%4!=0 or regmem[rs]+int(address,2) > 128 ):
        print("Wrong memory address! Exiting")
        exit()
    print("Loading value: "+str(data_mem[regmem[rs]+int(address,2)])+" to "+str(regmem_name[rt]))
    regmem[rt]=data_mem[regmem[rs]+int(address,2)]

def storeword(rs,rt,address):
    global data_mem
    if((regmem[rs]+int(address,2))%4!=0 or regmem[rs]+int(address,2) > 128 ):
        print("Wrong memory address! Exiting")
    print("Storing value: "+str(data_mem[regmem[rs]+int(address,2)])+" from "+str(regmem_name[rt]))
    data_mem[int(address,2)+regmem[rs]]=regmem[rt]

def jump_to(jump):
    global pc
    #print("jumpto fun")
    pc=int(hex(int(jump,2)), 16)
    print("Jumping to Instruction at memory: "+hex(pc))

def beq(rs, rt, address):
    global pc, regmem
    btarget= pc+(int(address,2)*4)
    #print(address)
    print(str(regmem_name[rs])+":"+str(regmem[rs]) + " " +str(regmem_name[rt])+":"+ str(regmem[rt]))
    #print(str(rs) + " " + str(rt))
    if(regmem[rs]-regmem[rt]==0):
        print("Equal")
        pc=btarget
    else:
        print("Not Equal")
        return


def fetch():
    global pc, cycle_count
    cycle_count+=1
    pc_original=pc
    # print(type(pc))
    # print(type(0x4))
    pc=pc+0x4
    #print(pc_original)
    #print(str(pc) + "fetch")
    return instruction_mem[pc_original]

def decode(inp):
    global rs, rt, rd, op, address, fn, jump
    print("\n")
    op = inp[0:6]
    print("Cycle : "+str(cycle_count))
    print(op)
    if(op=='000000'):
        rs=inp[6:11]
        rt=inp[11:16]
        rd=inp[16:21]
        shamt=inp[21:26]
        fn=inp[26:32]
        print("Decode")
    elif(op == '001000' or op=='100011' or op=='101011' or op=='000100'):
        rs=inp[6:11]
        rt=inp[11:16]
        address=inp[16:32]
        print("Decode")
    elif(op == '000010'):
        print("Decode")
        jump="0000"+inp[6:32]+"00"
        #print("jump to " + jump + hex(int(jump, 2)))

def execute():
    global op
    global fn
    if(op=='000000' and fn=='100000'):
        print("Execute add")
        add(rs,rt,rd)
    elif(op=='000000' and fn=='100010'):
        print("Execute sub")
        sub(rs,rt,rd)
    elif(op=='001000'):
        print("Execute addi")
        addi(rs,rt,address)
    elif(op=='100011'):
        print("Execute lw")
        loadword(rs,rt,address)
    elif(op=='101011'):
        print('Execute sw')
        storeword(rs,rt,address)
    elif(op=='000100'):
        print("Execute beq") 
        beq(rs,rt,address)
    elif(op == '000010'):
        print('Execute jump')
        jump_to(jump)
                


def main():
    global pc
    
    file1=open("instructions.txt","r")
    newlist=file1.readlines()
    j=0
    createInstructionMem()
    for i in instruction_mem:
        if(j<len(newlist)):
            s=newlist[j].rstrip('\n')
            instruction_mem[i]=s
        if(i == 0x00000000):
            end = i
        j+=1
    #print(instruction_mem)
    current_ins=-1
    while(current_ins != '00000000000000000000000000000000'):
        current_ins=fetch()
        #print(current_ins + "LOL" + str(type(current_ins)))
        decode(current_ins)
        execute()
        #print(str(i) + "main")
    #op = current_ins[0:6]
    #print(op)
    #print("inside")
    print("Exiting\n")
    print("Final Registers:\n")

    for i in regmem:
        print(regmem_name[i]+"  :  "+str(regmem[i]))
    print("Number of Cycles: "+str(cycle_count))
    #print(data_mem)

def createInstructionMem():
    global instruction_mem
    instruction_mem[0x00400000] = "0x00000000"
    instruction_mem[0x00400004] = "0x00000000"
    instruction_mem[0x00400008] = "0x00000000"
    instruction_mem[0x0040000c] = "0x00000000"
    instruction_mem[0x00400010] = "0x00000000"
    instruction_mem[0x00400014] = "0x00000000"
    instruction_mem[0x00400018] = "0x00000000"
    instruction_mem[0x0040001c] = "0x00000000"
    instruction_mem[0x00400020] = "0x00000000"
    instruction_mem[0x00400024] = "0x00000000"
    instruction_mem[0x00400028] = "0x00000000"
    instruction_mem[0x0040002c] = "0x00000000"
    instruction_mem[0x00400030] = "0x00000000"
    instruction_mem[0x00400034] = "0x00000000"
    instruction_mem[0x00400038] = "0x00000000"
    instruction_mem[0x0040003c] = "0x00000000"
    instruction_mem[0x00400040] = "0x00000000"
    instruction_mem[0x00400044] = "0x00000000"
    instruction_mem[0x00400048] = "0x00000000"
    instruction_mem[0x0040004c] = "0x00000000"
    instruction_mem[0x00400050] = "0x00000000"
    instruction_mem[0x00400054] = "0x00000000"
    instruction_mem[0x00400058] = "0x00000000"
    instruction_mem[0x0040005c] = "0x00000000"
    instruction_mem[0x00400060] = "0x00000000"
    instruction_mem[0x00400064] = "0x00000000"
    instruction_mem[0x00400068] = "0x00000000"
    instruction_mem[0x0040006c] = "0x00000000"
    instruction_mem[0x00400070] = "0x00000000"
    instruction_mem[0x00400074] = "0x00000000"
    instruction_mem[0x00400078] = "0x00000000"
    instruction_mem[0x0040007c] = "0x00000000"

if __name__ == "__main__":
    main()