#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *

class TestSuite:
    def test(self):
        # 66 0F 75 /r
        # pcmpeqw mm1, mm2/m64
        Buffer = '660f759011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf75')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pcmpeqw ')
        assert_equal(myDisasm.instr.repr, 'pcmpeqw xmm2, xmmword ptr [rax+44332211h]')

        # VEX.NDS.128.66.0F.WIG 75 /r
        # vpcmpeqw xmm1, xmm2, xmm3/m128
        Buffer = 'c40101750e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqw ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqw xmm9, xmm15, xmmword ptr [r14]')

        # VEX.NDS.256.66.0F.WIG 75 /r
        # vpcmpeqw ymm1, ymm2, ymm3/m256
        Buffer = 'c40105750e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqw ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqw ymm9, ymm15, ymmword ptr [r14]')

        # EVEX.NDS.128.66.0F.WIG 75 /r
        # vpcmpeqw xmm1 {k1}{z}, xmm2, xmm3/m128
        Buffer = '62010506750e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x1)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x75')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqw ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqw xmm1, xmm15, xmmword ptr [rsi]')

        # EVEX.NDS.256.66.0F.WIG 75 /r
        # vpcmpeqw ymm1 {k1}{z}, ymm2, ymm3/m256
        Buffer = '62010520750e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x1)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x75')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqw ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqw ymm1, ymm15, ymmword ptr [rsi]')

        # EVEX.NDS.512.66.0F.WIG 75 /r
        # vpcmpeqw zmm1 {k1}{z}, zmm2, zmm3/m512
        Buffer = '62010540750e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x1)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x75')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqw ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqw zmm1, zmm15, zmmword ptr [rsi]')
