from BitVector import *
import numpy as np
import time
import copy
import binascii
import codecs

rc = "01"
en_msg = ""
de_msg = ""
e_time = 0
d_time = 0
key_time = 0
SB = []
ISB = []


"""Tables"""
Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"),
     BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"),
     BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"),
     BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"),
     BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"),
     BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"),
     BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"),
     BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"),
     BitVector(hexstring="09"), BitVector(hexstring="0E")]
]


def hex_conv(name):
    # Iterate over the string
    data = []
    for element in name:
        data.append(format(ord(element), "x"))
    # print(data)
    return data


def key_gen(arr_2d, d):
    y = d[0]
    for i in range(3):
        d[i] = d[i+1]
    d[3] = y
    # print(d)
    # print("\n")

    for i in range(4):
        x = lookup_table(d[i])
        d[i] = x
    # print(d)

    return d


def lookup_table(x):
    b = BitVector(hexstring=x)
    int_val = b.intValue()
    s = Sbox[int_val]
    s = BitVector(intVal=s, size=8)
    s1 = s.get_bitvector_in_hex()
    return s1
    # print(s1)


def inv_lookup_table(x):
    b = BitVector(hexstring=x)
    int_val = b.intValue()
    s = InvSbox[int_val]
    s = BitVector(intVal=s, size=8)
    s1 = s.get_bitvector_in_hex()
    return s1


def rnd_cnst(i, d):
    global rc
    if(i == 1):
        #print(hex(int("01",16) ^ int(d[0],16)))
        a = hex(int("01", 16) ^ int(d[0], 16))[2:]
        rc = "01"
        #m = format(a.intValue(), "02x")
        # print(a)
        d[0] = a
        return d

    else:
        AES_modulus = BitVector(bitstring='100011011')

        bv1 = BitVector(hexstring="02")
        bv2 = BitVector(hexstring=rc)
        bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
        # print(bv3)
        rc = bv3.get_bitvector_in_hex()

        #print(hex(int(rc,16) ^ int(d[0],16)))
        a = hex(int(rc, 16) ^ int(d[0], 16))[2:]
        #m = format(a.intValue(), "02x")
        # print(a)
        d[0] = a
        return d


def go(samp, f_data):

    for j in range(1, 11):
        data3 = []
        for i in range(4):
            data3.append(samp[i][3])

        z = key_gen(samp, data3)

        p = rnd_cnst(j, z)

        for i in range(4):  # first column only
            samp[i][0] = hex(int(p[i], 16) ^ int(samp[i][0], 16))[2:]
            # print(samp[i][0])

        for i in range(1, 4):  # for column
            for k in range(4):  # for row
                samp[k][i] = hex(int(samp[k][i-1], 16) ^
                                 int(samp[k][i], 16))[2:]

        samp_f = []
        samp_f = copy.deepcopy(samp)
        f_data.append(samp_f)

    # out of 11th loop
    return f_data


def prep(fix):
    g = []
    for i in range(4):
        for j in range(4):
            x = hex(int("00", 16) ^ int(fix[i][j], 16))[2:]
            g.append(x)
    arr1 = np.array(g)
    fix = np.reshape(arr1, (4, 4), order='F')

    # print(fix)
    return fix


def anti_prep(A):
    for i in range(4):
        for j in range(4):
            A[i][j] = int(A[i][j], 16)

    # print(A)
    return A


def mult(x, y):
    AES_modulus = BitVector(bitstring='100011011')

    bv1 = BitVector(hexstring=x)
    bv2 = BitVector(hexstring=y)
    bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
    # print(bv3)
    #r = bv3.get_bitvector_in_hex()
    return bv3


def encrypt(en_2d, f_data):
    fix = [["02", "03", "01", "01"], ["01", "02", "03", "01"],
           ["01", "01", "02", "03"], ["03", "01", "01", "02"]]

    for v in range(1, 11):
        for i in range(4):
            for j in range(4):
                en_2d[i][j] = lookup_table(en_2d[i][j])  # SUBSTITUTION
        # print(en_2d)
        # ROW_SHIFT
        for i in range(4):
            y = []
            y = np.roll(en_2d[i], -i)
            en_2d[i] = y
        # print("\ntest:\n")
        # print(en_2d)

        # MATRIX_MULTIPLICATION
        if(v != 10):
            result = copy.deepcopy(en_2d)
            A = fix
            B = en_2d
            #C = np.matmul(fix,en_2d)
            #print("after multi:\n")
            for i in range(len(fix)):
                for j in range(len(en_2d[0])):
                    d = []
                    for k in range(len(en_2d)):
                        h = mult(fix[i][k], en_2d[k][j])
                        d.append(h)
                    d1 = d[0] ^ d[1]
                    d2 = d[2] ^ d[3]
                    d4 = d1 ^ d2
                    result[i][j] = d4.get_bitvector_in_hex()
            en_2d = result
            # print(en_2d)

        # Add round key
        #rck = f_data[v]
        for i in range(4):
            for j in range(4):
                en_2d[i][j] = hex(int(en_2d[i][j], 16) ^
                                  int(f_data[v][i][j], 16))[2:]

    # print(en_2d)
    return en_2d


def decrypt(en_2d, f_data):
    inv_fix = [["0E", "0B", "0D", "09"],
               ["09", "0E", "0B", "0D"],
               ["0D", "09", "0E", "0B"],
               ["0B", "0D", "09", "0E"]]

    for v in range(9, -1, -1):
        # INV_SHIFT_ROW
        for i in range(4):
            y = []
            y = np.roll(en_2d[i], i)
            en_2d[i] = y
        # print(en_2d)

        # SUBSTITUTE_INV_BYTES
        for i in range(4):
            for j in range(4):
                en_2d[i][j] = inv_lookup_table(en_2d[i][j])  # SUBSTITUTION
        # print(en_2d)

        # ADD ROUND KEY
        for i in range(4):
            for j in range(4):
                en_2d[i][j] = hex(int(en_2d[i][j], 16) ^
                                  int(f_data[v][i][j], 16))[2:]
        # print(en_2d)

        # INV_MULT
        if(v != 0):
            result = copy.deepcopy(en_2d)

            #print("after multi:\n")
            for i in range(len(inv_fix)):
                for j in range(len(en_2d[0])):
                    d = []
                    for k in range(len(en_2d)):
                        h = mult(inv_fix[i][k], en_2d[k][j])
                        d.append(h)
                    d1 = d[0] ^ d[1]
                    d2 = d[2] ^ d[3]
                    d4 = d1 ^ d2
                    result[i][j] = d4.get_bitvector_in_hex()
            en_2d = result
            # print(en_2d)
        # print(en_2d)
    return en_2d


def get_inv_sbox():
    #global SB
    global ISB
    cv = BitVector(hexstring="05")
    #cv = cv.reverse()
    modulus = BitVector(bitstring='100011011')
    n = 8
    a = BitVector(hexstring=SB[0])
    s = a.gf_MI(modulus, n)
    s = BitVector(bitstring=s)
    #s = s.reverse()
    a = s << 1
    b = s << 3
    c = s << 6

    p = a ^ b
    q = c ^ cv

    s = p ^ q
    # print(s)
    print(s.get_bitvector_in_hex())
    # print(s)
    # print(s.reverse())

    # for i in range(256):

    #     bv = BitVector(bitstring = '00000000')
    #     # bv.reverse()
    #     modulus = BitVector(bitstring = '100011011')
    #     n = 8
    #     a = BitVector(hexstring = SB[i])
    #     s = a.gf_MI(modulus, n)
    #     s = BitVector(bitstring = s)
    # print(type(s))
    # print(bv)
    # bv = s.reverse()
    # test = BitVector(bitstring = '00000000')
    # for i in range(8):
    #     x = bv[(i+4)%8] ^ bv[(i+6)%8]
    #     y = cv[i] ^ bv[(i+9)%8]
    #     test[i] = x ^ y

    # test = test.reverse()
    # test = BitVector(bitstring = test)
    # ISB.append(test.get_bitvector_in_hex())
    #s = s.reverse()
    # a = s<<1
    # b = s<<3
    # c = s<<6

    # p = a ^ b
    # q = c ^ cv

    # s = p ^ q
    # # s = BitVector(bitstring = s)
    # # s = s.reverse()
    # ISB.append(s.get_bitvector_in_hex())
    # arr = np.array(ISB)
    # arr_2d = arr.reshape(16,16)
    # print(arr_2d)
    # print(ISB)


def get_sbox():
    global SB
    for i in range(0, 256):
        r = hex(i)[2:]
        if i != 0:
            modulus = BitVector(bitstring='100011011')
            n = 8
            a = BitVector(hexstring=r)
            bv = a.gf_MI(modulus, n)
            # print(bv)
            bv = bv.reverse()
            #print("after: ",bv)
        if i == 0:
            bv = BitVector(bitstring='00000000')

        cv = BitVector(bitstring='01100011')
        cv = cv.reverse()
        #print("after: ",cv)

        test = BitVector(bitstring='00000000')

        for i in range(8):
            x = bv[i] ^ bv[(i+4) % 8]
            y = bv[(i+5) % 8] ^ bv[(i+6) % 8]
            z = cv[i] ^ bv[(i+7) % 8]
            m = x ^ y
            p = m ^ z
            test[i] = p

        test = test.reverse()
        test = BitVector(bitstring=test)
        SB.append(test.get_bitvector_in_hex())

    arr = np.array(SB)
    arr_2d = arr.reshape(16, 16)
    print(arr_2d)


def start(key, msg):
    global en_msg
    global de_msg
    global e_time
    global d_time
    global key_time

    en_d = []
    en_2d = []
    samp = []
    f_data = []
    data2 = []

    s1 = time.time()
    data2 = hex_conv(key)
    arr = np.array(data2)
    arr_2d = np.reshape(arr, (4, 4), order='F')
    f_data.append(arr_2d)
    samp = copy.deepcopy(arr_2d)
    f_data = go(samp, f_data)
    e1 = time.time()

    key_time = e1-s1

    # ENCRYPTION

    s2 = time.time()
    en_d = hex_conv(msg)
    arr1 = np.array(en_d)
    en_2d = np.reshape(arr1, (4, 4), order='F')

    # print("\nEncrypted:")
    #print("Ciphered Text:")
    for i in range(4):
        for j in range(4):
            en_2d[i][j] = hex(int(en_2d[i][j], 16) ^
                              int(f_data[0][i][j], 16))[2:]

    # print(en_2d)
    # print("encrypted:\n")
    en_2d = encrypt(en_2d, f_data)
    arr = np.array(en_2d)
    arr_2d = np.reshape(arr, 16, order='F')
    # print(arr_2d)
    e2 = time.time()

    str1 = ""

    for ele in arr_2d:
        str1 += ele
    #print(str1,"[In HEX]",sep=" ")
    en_msg += str1

    e_time += e2 - s2

    # DECRYPTION
    # print("\nDecrypted:")
    #print("Decrypted Text:")

    s3 = time.time()
    for i in range(4):
        for j in range(4):
            en_2d[i][j] = hex(int(en_2d[i][j], 16) ^
                              int(f_data[10][i][j], 16))[2:]

    # print(en_2d)
    en_2d = decrypt(en_2d, f_data)

    # print(en_2d)
    arr = np.array(en_2d)
    arr_2d = np.reshape(arr, 16, order='F')
    # print(arr_2d)
    e3 = time.time()

    str1 = ""

    for ele in arr_2d:
        str1 += ele
    #print(str1,"[In HEX]",sep=" ")
    de_msg += str1

    str2 = ""
    for s in arr_2d:
        str2 += bytearray.fromhex(s).decode()

    d_time += e3 - s3

    #print(str2,"[In ASCII]",sep=" ")


def main():

    key = "BUET CSE16 Batch"
    # msg = "WillGraduateSoon"
    #key = "Thats my Kung Fu"
    #msg = "Two One Nine Two"
    # key = input('Enter Key: ')
    # msg = input('Enter msg: ')

    #filename = input('Enter filename:')
    filename = 'Untitled2.png'
    with open(filename, 'rb') as f:
        content = f.read()
    x= binascii.hexlify(content)
    msg = str(binascii.hexlify(content), 'ascii')

    # print(msg)
    #msg = "WillGraduateSoon"

    if len(key) < 16:
        while len(key) < 16:
            key = key + "0"
    if len(key) > 16:
        key = key[:16]

    k = hex_conv(key)
    str1 = ""
    for w in k:
        str1 += w

    print("Plain text:")
    print("Key:")
    print(key, "[In ASCII]", sep=" ")
    print(str1, "[In HEX]", sep=" ")
    print()
    k = hex_conv(msg)
    str1 = ""
    for w in k:
        str1 += w
    # print(msg,"[In ASCII]",sep=" ")
    # print(str1,"[In HEX]",sep=" ")

    n = 16
    chunks = [msg[i:i+n] for i in range(0, len(msg), n)]
    # print(chunks)
    s = chunks[len(chunks)-1]
    if len(s) < 16:
        while len(s) < 16:
            s = s+" "
    chunks[len(chunks)-1] = s

    for c in chunks:
        start(key, c)

    # start(key,msg)

    print("\nEncrypted:")
    print("Encrypted Text:")
    print(en_msg, "[In HEX]", sep=" ")
    #str2 = bytearray.fromhex(en_msg).decode()
    #print(str2,"[In ASCII]",sep=" ")

    print("\nDecrypted:")
    print("Decrypted Text:")
    print(de_msg, "[In HEX]", sep=" ")

    str2 = bytearray.fromhex(de_msg).decode()
    print(str2, "[In ASCII]", sep=" ")

    print("\nExecution Time:")
    print("Key scheduling:", key_time)
    print("Encryption Time:", e_time)
    print("Decryption Time:", d_time)

    print("\nS-Box:")
    get_sbox()
    print("\nInverse S-Box:")
    # get_inv_sbox()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
