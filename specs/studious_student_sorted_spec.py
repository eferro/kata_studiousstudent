# -*- coding: utf-8 -*-

from expects import *
from hamcrest import *
from doublex import *

from studiousstudents import studiousstudents

with describe('studious students'):
    with describe('sorter'):
        with it('base examples'):
            expect(studiousstudents.StudiousStudentsSorter().sort('6 facebook hacker cup for studious students')).to(equal('cupfacebookforhackerstudentsstudious'))
            expect(studiousstudents.StudiousStudentsSorter().sort('5 k duz q rc lvraw')).to(equal('duzklvrawqrc'))
            expect(studiousstudents.StudiousStudentsSorter().sort('5 mybea zdr yubx xe dyroiy')).to(equal('dyroiymybeaxeyubxzdr'))
            expect(studiousstudents.StudiousStudentsSorter().sort('5 uiuy hopji li j dcyi')).to(equal('dcyihopjijliuiuy'))
            expect(studiousstudents.StudiousStudentsSorter().sort('5 jibw ji jp bw jibw')).to(equal('bwjibwjibwjijp'))
        
        with it('sorted final word, not order of the tokens'):
            expect(studiousstudents.StudiousStudentsSorter().sort('5 ca c')).to(equal('cac'))
