# This file was automatically created by FeynRules 2.0.20
# Mathematica version: 9.0 for Microsoft Windows (64-bit) (January 25, 2013)
# Date: Wed 12 Mar 2014 02:18:26


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = '-2*FM0*complex(0,1) - FM6*complex(0,1)',
                order = {'NP':1})

GC_5 = Coupling(name = 'GC_5',
                value = '-2*cw**2*FM0*complex(0,1) - cw**2*FM6*complex(0,1)',
                order = {'NP':1})

GC_6 = Coupling(name = 'GC_6',
                value = 'ee**2*FM0*complex(0,1) + (ee**2*FM6*complex(0,1))/2.',
                order = {'NP':1,'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-(FM1*complex(0,1))/2. + (FM7*complex(0,1))/4.',
                order = {'NP':1})

GC_8 = Coupling(name = 'GC_8',
                value = '-(ee*FM7*complex(0,1))/8.',
                order = {'NP':1,'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = '-(ee**2*FM7*complex(0,1))/4.',
                order = {'NP':1,'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(cw**2*FM1*complex(0,1))/2. + (cw**2*FM7*complex(0,1))/4.',
                 order = {'NP':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '(ee**2*FM1*complex(0,1))/4. - (ee**2*FM7*complex(0,1))/8.',
                 order = {'NP':1,'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '2*complex(0,1)*FS0 + 2*complex(0,1)*FS1',
                 order = {'NP':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '8*complex(0,1)*FT0',
                 order = {'NP':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '8*cw**2*complex(0,1)*FT0',
                 order = {'NP':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '4*complex(0,1)*FT1',
                 order = {'NP':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '4*cw**2*complex(0,1)*FT1',
                 order = {'NP':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '8*cw**4*complex(0,1)*FT0 + 8*cw**4*complex(0,1)*FT1',
                 order = {'NP':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '2*complex(0,1)*FT2',
                 order = {'NP':1})

GC_19 = Coupling(name = 'GC_19',
                 value = 'cw**2*complex(0,1)*FT2',
                 order = {'NP':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '2*cw**4*complex(0,1)*FT2',
                 order = {'NP':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-G',
                 order = {'QCD':1})

GC_22 = Coupling(name = 'GC_22',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_23 = Coupling(name = 'GC_23',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_24 = Coupling(name = 'GC_24',
                 value = 'cw*complex(0,1)*gw',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(cw*ee*FM7*complex(0,1)*gw)/8.',
                 order = {'NP':1,'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '(ee**2*FM7*complex(0,1)*gw)/(8.*cw)',
                 order = {'NP':1,'QED':3})

GC_27 = Coupling(name = 'GC_27',
                 value = '(cw*ee**2*FM7*complex(0,1)*gw)/2.',
                 order = {'NP':1,'QED':3})

GC_28 = Coupling(name = 'GC_28',
                 value = '-8*cw*complex(0,1)*FT0*gw',
                 order = {'NP':1,'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '-8*cw**3*complex(0,1)*FT0*gw',
                 order = {'NP':1,'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '8*cw*complex(0,1)*FT1*gw',
                 order = {'NP':1,'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '4*cw**3*complex(0,1)*FT1*gw',
                 order = {'NP':1,'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '-(cw*complex(0,1)*FT2*gw)',
                 order = {'NP':1,'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '-(cw**3*complex(0,1)*FT2*gw)',
                 order = {'NP':1,'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '-(complex(0,1)*gw**2)',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = 'cw**2*complex(0,1)*gw**2',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = 'ee**2*FM1*complex(0,1)*gw**2',
                 order = {'NP':1,'QED':4})

GC_37 = Coupling(name = 'GC_37',
                 value = '-(ee**2*FM7*complex(0,1)*gw**2)',
                 order = {'NP':1,'QED':4})

GC_38 = Coupling(name = 'GC_38',
                 value = '(-3*ee**2*FM7*complex(0,1)*gw**2)/2.',
                 order = {'NP':1,'QED':4})

GC_39 = Coupling(name = 'GC_39',
                 value = '8*complex(0,1)*FT0*gw**2',
                 order = {'NP':1,'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '8*cw**2*complex(0,1)*FT0*gw**2',
                 order = {'NP':1,'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '-8*cw**4*complex(0,1)*FT0*gw**2',
                 order = {'NP':1,'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '4*complex(0,1)*FT1*gw**2',
                 order = {'NP':1,'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '4*cw**2*complex(0,1)*FT1*gw**2',
                 order = {'NP':1,'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '-4*cw**4*complex(0,1)*FT1*gw**2',
                 order = {'NP':1,'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '2*complex(0,1)*FT2*gw**2',
                 order = {'NP':1,'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '2*cw**2*complex(0,1)*FT2*gw**2',
                 order = {'NP':1,'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(cw**4*complex(0,1)*FT2*gw**2)',
                 order = {'NP':1,'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '-8*cw*complex(0,1)*FT0*gw**3',
                 order = {'NP':1,'QED':3})

GC_49 = Coupling(name = 'GC_49',
                 value = '8*cw**3*complex(0,1)*FT0*gw**3',
                 order = {'NP':1,'QED':3})

GC_50 = Coupling(name = 'GC_50',
                 value = '4*cw*complex(0,1)*FT1*gw**3',
                 order = {'NP':1,'QED':3})

GC_51 = Coupling(name = 'GC_51',
                 value = '-8*cw**3*complex(0,1)*FT1*gw**3',
                 order = {'NP':1,'QED':3})

GC_52 = Coupling(name = 'GC_52',
                 value = '-2*cw*complex(0,1)*FT2*gw**3',
                 order = {'NP':1,'QED':3})

GC_53 = Coupling(name = 'GC_53',
                 value = '-2*cw**3*complex(0,1)*FT2*gw**3',
                 order = {'NP':1,'QED':3})

GC_54 = Coupling(name = 'GC_54',
                 value = '-8*cw**2*complex(0,1)*FT0*gw**4',
                 order = {'NP':1,'QED':4})

GC_55 = Coupling(name = 'GC_55',
                 value = '16*cw**4*complex(0,1)*FT0*gw**4',
                 order = {'NP':1,'QED':4})

GC_56 = Coupling(name = 'GC_56',
                 value = '-16*cw**2*complex(0,1)*FT1*gw**4',
                 order = {'NP':1,'QED':4})

GC_57 = Coupling(name = 'GC_57',
                 value = '16*cw**4*complex(0,1)*FT1*gw**4',
                 order = {'NP':1,'QED':4})

GC_58 = Coupling(name = 'GC_58',
                 value = '-4*cw**2*complex(0,1)*FT2*gw**4',
                 order = {'NP':1,'QED':4})

GC_59 = Coupling(name = 'GC_59',
                 value = '8*cw**4*complex(0,1)*FT2*gw**4',
                 order = {'NP':1,'QED':4})

GC_60 = Coupling(name = 'GC_60',
                 value = '2*cw*FM0*complex(0,1)*gw + cw*FM6*complex(0,1)*gw',
                 order = {'NP':1,'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(cw*FM1*complex(0,1)*gw)/2. + (cw*FM7*complex(0,1)*gw)/4.',
                 order = {'NP':1,'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-2*FM0*complex(0,1)*gw**2 - FM6*complex(0,1)*gw**2',
                 order = {'NP':1,'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '2*cw**2*FM0*complex(0,1)*gw**2 + cw**2*FM6*complex(0,1)*gw**2',
                 order = {'NP':1,'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '-(ee**2*FM0*complex(0,1)*gw**2) - (ee**2*FM6*complex(0,1)*gw**2)/2.',
                 order = {'NP':1,'QED':4})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(FM1*complex(0,1)*gw**2) + (FM7*complex(0,1)*gw**2)/2.',
                 order = {'NP':1,'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = 'cw**2*FM1*complex(0,1)*gw**2 - (cw**2*FM7*complex(0,1)*gw**2)/2.',
                 order = {'NP':1,'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '24*complex(0,1)*FT0*gw**4 + 24*complex(0,1)*FT1*gw**4 + 12*complex(0,1)*FT2*gw**4',
                 order = {'NP':1,'QED':4})

GC_68 = Coupling(name = 'GC_68',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '(ee**2*FM0*complex(0,1))/sw**2 + (ee**2*FM6*complex(0,1))/(2.*sw**2)',
                 order = {'NP':1,'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(cw**2*ee**2*FM0*complex(0,1))/sw**2 + (cw**2*ee**2*FM6*complex(0,1))/(2.*sw**2)',
                 order = {'NP':1,'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '(3*ee**4*complex(0,1)*FS0)/(2.*cw**2) + (3*cw**2*ee**4*complex(0,1)*FS0)/(2.*sw**4) + (3*ee**4*complex(0,1)*FS0)/sw**2',
                 order = {'NP':1,'QED':4})

GC_72 = Coupling(name = 'GC_72',
                 value = '(3*ee**4*complex(0,1)*FS1)/cw**2 + (3*cw**2*ee**4*complex(0,1)*FS1)/sw**4 + (6*ee**4*complex(0,1)*FS1)/sw**2',
                 order = {'NP':1,'QED':4})

GC_73 = Coupling(name = 'GC_73',
                 value = '-((cw*ee**2*FM0*complex(0,1)*gw)/sw**2) - (cw*ee**2*FM6*complex(0,1)*gw)/(2.*sw**2)',
                 order = {'NP':1,'QED':3})

GC_74 = Coupling(name = 'GC_74',
                 value = '-((cw**2*ee**2*FM0*complex(0,1)*gw**2)/sw**2) - (cw**2*ee**2*FM6*complex(0,1)*gw**2)/(2.*sw**2)',
                 order = {'NP':1,'QED':4})

GC_75 = Coupling(name = 'GC_75',
                 value = '(3*ee**2*FM0*complex(0,1)*gw**2)/sw**2 - (3*ee**2*FM1*complex(0,1)*gw**2)/(2.*sw**2) + (3*ee**2*FM6*complex(0,1)*gw**2)/(2.*sw**2) + (3*ee**2*FM7*complex(0,1)*gw**2)/(4.*sw**2)',
                 order = {'NP':1,'QED':4})

GC_76 = Coupling(name = 'GC_76',
                 value = '(cw*ee**2*FM0*complex(0,1))/sw + (cw*ee**2*FM6*complex(0,1))/(2.*sw)',
                 order = {'NP':1,'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '(-3*cw*ee**3*complex(0,1)*FS0)/(4.*sw**3) - (3*ee**3*complex(0,1)*FS0)/(4.*cw*sw)',
                 order = {'NP':1,'QED':3})

GC_78 = Coupling(name = 'GC_78',
                 value = '-((ee**2*FM0*complex(0,1)*gw)/sw) - (ee**2*FM6*complex(0,1)*gw)/(2.*sw)',
                 order = {'NP':1,'QED':3})

GC_79 = Coupling(name = 'GC_79',
                 value = '(4*cw*ee**2*FM0*complex(0,1)*gw**2)/sw + (2*cw*ee**2*FM6*complex(0,1)*gw**2)/sw',
                 order = {'NP':1,'QED':4})

GC_80 = Coupling(name = 'GC_80',
                 value = '(6*ee**4*complex(0,1)*FS0)/sw**4',
                 order = {'NP':1,'QED':4})

GC_81 = Coupling(name = 'GC_81',
                 value = '(3*ee**4*complex(0,1)*FS1)/sw**4',
                 order = {'NP':1,'QED':4})

GC_82 = Coupling(name = 'GC_82',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '-(ee**2*FM1*complex(0,1))/(4.*sw**2)',
                 order = {'NP':1,'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '(cw**2*ee**2*FM1*complex(0,1))/(4.*sw**2)',
                 order = {'NP':1,'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '(ee**2*FM7*complex(0,1))/(4.*sw**2)',
                 order = {'NP':1,'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '-(cw**2*ee**2*FM7*complex(0,1))/(8.*sw**2)',
                 order = {'NP':1,'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '-(ee**2*complex(0,1)*FS0)/(2.*sw**2)',
                 order = {'NP':1,'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '-((ee**2*complex(0,1)*FS1)/sw**2)',
                 order = {'NP':1,'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '(cw*ee**2*FM1*complex(0,1)*gw)/(4.*sw**2)',
                 order = {'NP':1,'QED':3})

GC_90 = Coupling(name = 'GC_90',
                 value = '(cw*ee**2*FM7*complex(0,1)*gw)/(8.*sw**2)',
                 order = {'NP':1,'QED':3})

GC_91 = Coupling(name = 'GC_91',
                 value = '(3*cw**3*ee**2*FM7*complex(0,1)*gw)/(8.*sw**2)',
                 order = {'NP':1,'QED':3})

GC_92 = Coupling(name = 'GC_92',
                 value = '(3*cw**2*ee**2*FM1*complex(0,1)*gw**2)/(2.*sw**2)',
                 order = {'NP':1,'QED':4})

GC_93 = Coupling(name = 'GC_93',
                 value = '(-9*cw**2*ee**2*FM7*complex(0,1)*gw**2)/(4.*sw**2)',
                 order = {'NP':1,'QED':4})

GC_94 = Coupling(name = 'GC_94',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(cw*ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-(cw*ee**2*FM1*complex(0,1))/(4.*sw)',
                  order = {'NP':1,'QED':2})

GC_102 = Coupling(name = 'GC_102',
                  value = '-(cw*ee*FM7*complex(0,1))/(8.*sw)',
                  order = {'NP':1,'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '(cw*ee**2*FM7*complex(0,1))/(8.*sw)',
                  order = {'NP':1,'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '-(ee**2*FM1*complex(0,1)*gw)/(4.*sw)',
                  order = {'NP':1,'QED':3})

GC_105 = Coupling(name = 'GC_105',
                  value = '(ee*FM7*complex(0,1)*gw)/(8.*sw)',
                  order = {'NP':1,'QED':2})

GC_106 = Coupling(name = 'GC_106',
                  value = '-(cw**2*ee*FM7*complex(0,1)*gw)/(8.*sw)',
                  order = {'NP':1,'QED':2})

GC_107 = Coupling(name = 'GC_107',
                  value = '(ee**2*FM7*complex(0,1)*gw)/(4.*sw)',
                  order = {'NP':1,'QED':3})

GC_108 = Coupling(name = 'GC_108',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*gw)/(8.*sw)',
                  order = {'NP':1,'QED':3})

GC_109 = Coupling(name = 'GC_109',
                  value = '-((cw*ee**2*FM1*complex(0,1)*gw**2)/sw)',
                  order = {'NP':1,'QED':4})

GC_110 = Coupling(name = 'GC_110',
                  value = '-(cw*ee**2*FM7*complex(0,1)*gw**2)/(2.*sw)',
                  order = {'NP':1,'QED':4})

GC_111 = Coupling(name = 'GC_111',
                  value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-(ee*FM7*complex(0,1)*sw)/(8.*cw)',
                  order = {'NP':1,'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(ee**2*FM7*complex(0,1)*sw)/(8.*cw)',
                  order = {'NP':1,'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '8*cw*complex(0,1)*FT0*sw',
                  order = {'NP':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '4*cw*complex(0,1)*FT1*sw',
                  order = {'NP':1})

GC_117 = Coupling(name = 'GC_117',
                  value = 'cw*complex(0,1)*FT2*sw',
                  order = {'NP':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '2*cw**3*complex(0,1)*FT2*sw',
                  order = {'NP':1})

GC_119 = Coupling(name = 'GC_119',
                  value = 'complex(0,1)*gw*sw',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-(ee*FM7*complex(0,1)*gw*sw)/8.',
                  order = {'NP':1,'QED':2})

GC_121 = Coupling(name = 'GC_121',
                  value = '-(ee**2*FM7*complex(0,1)*gw*sw)/4.',
                  order = {'NP':1,'QED':3})

GC_122 = Coupling(name = 'GC_122',
                  value = '-8*complex(0,1)*FT0*gw*sw',
                  order = {'NP':1,'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '-8*cw**2*complex(0,1)*FT0*gw*sw',
                  order = {'NP':1,'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '4*complex(0,1)*FT1*gw*sw',
                  order = {'NP':1,'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '4*cw**2*complex(0,1)*FT1*gw*sw',
                  order = {'NP':1,'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '-(complex(0,1)*FT2*gw*sw)',
                  order = {'NP':1,'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '-(cw**2*complex(0,1)*FT2*gw*sw)',
                  order = {'NP':1,'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '-2*cw*complex(0,1)*gw**2*sw',
                  order = {'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = '-(ee**2*FM7*complex(0,1)*gw**2*sw)/(2.*cw)',
                  order = {'NP':1,'QED':4})

GC_130 = Coupling(name = 'GC_130',
                  value = '8*cw*complex(0,1)*FT0*gw**2*sw',
                  order = {'NP':1,'QED':2})

GC_131 = Coupling(name = 'GC_131',
                  value = '16*cw**3*complex(0,1)*FT0*gw**2*sw',
                  order = {'NP':1,'QED':2})

GC_132 = Coupling(name = 'GC_132',
                  value = '4*cw*complex(0,1)*FT1*gw**2*sw',
                  order = {'NP':1,'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = '-4*cw**3*complex(0,1)*FT1*gw**2*sw',
                  order = {'NP':1,'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = 'cw*complex(0,1)*FT2*gw**2*sw',
                  order = {'NP':1,'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '-2*cw**3*complex(0,1)*FT2*gw**2*sw',
                  order = {'NP':1,'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = '-8*complex(0,1)*FT0*gw**3*sw',
                  order = {'NP':1,'QED':3})

GC_137 = Coupling(name = 'GC_137',
                  value = '-16*cw**2*complex(0,1)*FT0*gw**3*sw',
                  order = {'NP':1,'QED':3})

GC_138 = Coupling(name = 'GC_138',
                  value = '4*complex(0,1)*FT1*gw**3*sw',
                  order = {'NP':1,'QED':3})

GC_139 = Coupling(name = 'GC_139',
                  value = '-8*cw**2*complex(0,1)*FT1*gw**3*sw',
                  order = {'NP':1,'QED':3})

GC_140 = Coupling(name = 'GC_140',
                  value = 'complex(0,1)*FT2*gw**3*sw',
                  order = {'NP':1,'QED':3})

GC_141 = Coupling(name = 'GC_141',
                  value = '-6*cw**2*complex(0,1)*FT2*gw**3*sw',
                  order = {'NP':1,'QED':3})

GC_142 = Coupling(name = 'GC_142',
                  value = '48*cw*complex(0,1)*FT0*gw**4*sw',
                  order = {'NP':1,'QED':4})

GC_143 = Coupling(name = 'GC_143',
                  value = '-16*cw**3*complex(0,1)*FT0*gw**4*sw',
                  order = {'NP':1,'QED':4})

GC_144 = Coupling(name = 'GC_144',
                  value = '8*cw*complex(0,1)*FT1*gw**4*sw',
                  order = {'NP':1,'QED':4})

GC_145 = Coupling(name = 'GC_145',
                  value = '-16*cw**3*complex(0,1)*FT1*gw**4*sw',
                  order = {'NP':1,'QED':4})

GC_146 = Coupling(name = 'GC_146',
                  value = '12*cw*complex(0,1)*FT2*gw**4*sw',
                  order = {'NP':1,'QED':4})

GC_147 = Coupling(name = 'GC_147',
                  value = '-4*cw**3*complex(0,1)*FT2*gw**4*sw',
                  order = {'NP':1,'QED':4})

GC_148 = Coupling(name = 'GC_148',
                  value = '8*complex(0,1)*FT0*sw**2',
                  order = {'NP':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '4*complex(0,1)*FT1*sw**2',
                  order = {'NP':1})

GC_150 = Coupling(name = 'GC_150',
                  value = 'complex(0,1)*FT2*sw**2',
                  order = {'NP':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '2*cw**2*complex(0,1)*FT2*sw**2',
                  order = {'NP':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '(ee*FM7*complex(0,1)*gw*sw**2)/(8.*cw)',
                  order = {'NP':1,'QED':2})

GC_153 = Coupling(name = 'GC_153',
                  value = '-8*cw*complex(0,1)*FT0*gw*sw**2',
                  order = {'NP':1,'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '4*cw*complex(0,1)*FT1*gw*sw**2',
                  order = {'NP':1,'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '-(cw*complex(0,1)*FT2*gw*sw**2)',
                  order = {'NP':1,'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = 'complex(0,1)*gw**2*sw**2',
                  order = {'QED':2})

GC_157 = Coupling(name = 'GC_157',
                  value = '8*complex(0,1)*FT0*gw**2*sw**2',
                  order = {'NP':1,'QED':2})

GC_158 = Coupling(name = 'GC_158',
                  value = '-8*cw**2*complex(0,1)*FT0*gw**2*sw**2',
                  order = {'NP':1,'QED':2})

GC_159 = Coupling(name = 'GC_159',
                  value = '8*complex(0,1)*FT1*gw**2*sw**2',
                  order = {'NP':1,'QED':2})

GC_160 = Coupling(name = 'GC_160',
                  value = '-4*cw**2*complex(0,1)*FT1*gw**2*sw**2',
                  order = {'NP':1,'QED':2})

GC_161 = Coupling(name = 'GC_161',
                  value = '2*complex(0,1)*FT2*gw**2*sw**2',
                  order = {'NP':1,'QED':2})

GC_162 = Coupling(name = 'GC_162',
                  value = '-(cw**2*complex(0,1)*FT2*gw**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_163 = Coupling(name = 'GC_163',
                  value = '8*cw*complex(0,1)*FT0*gw**3*sw**2',
                  order = {'NP':1,'QED':3})

GC_164 = Coupling(name = 'GC_164',
                  value = '-8*cw*complex(0,1)*FT1*gw**3*sw**2',
                  order = {'NP':1,'QED':3})

GC_165 = Coupling(name = 'GC_165',
                  value = '-2*cw*complex(0,1)*FT2*gw**3*sw**2',
                  order = {'NP':1,'QED':3})

GC_166 = Coupling(name = 'GC_166',
                  value = '-8*complex(0,1)*FT0*gw**4*sw**2',
                  order = {'NP':1,'QED':4})

GC_167 = Coupling(name = 'GC_167',
                  value = '64*cw**2*complex(0,1)*FT0*gw**4*sw**2',
                  order = {'NP':1,'QED':4})

GC_168 = Coupling(name = 'GC_168',
                  value = '-16*complex(0,1)*FT1*gw**4*sw**2',
                  order = {'NP':1,'QED':4})

GC_169 = Coupling(name = 'GC_169',
                  value = '32*cw**2*complex(0,1)*FT1*gw**4*sw**2',
                  order = {'NP':1,'QED':4})

GC_170 = Coupling(name = 'GC_170',
                  value = '-4*complex(0,1)*FT2*gw**4*sw**2',
                  order = {'NP':1,'QED':4})

GC_171 = Coupling(name = 'GC_171',
                  value = '24*cw**2*complex(0,1)*FT2*gw**4*sw**2',
                  order = {'NP':1,'QED':4})

GC_172 = Coupling(name = 'GC_172',
                  value = '2*cw*complex(0,1)*FT2*sw**3',
                  order = {'NP':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '-8*complex(0,1)*FT0*gw*sw**3',
                  order = {'NP':1,'QED':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '4*complex(0,1)*FT1*gw*sw**3',
                  order = {'NP':1,'QED':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '-2*complex(0,1)*FT2*gw*sw**3',
                  order = {'NP':1,'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '-8*cw*complex(0,1)*FT0*gw**2*sw**3',
                  order = {'NP':1,'QED':2})

GC_177 = Coupling(name = 'GC_177',
                  value = '4*cw*complex(0,1)*FT1*gw**2*sw**3',
                  order = {'NP':1,'QED':2})

GC_178 = Coupling(name = 'GC_178',
                  value = 'cw*complex(0,1)*FT2*gw**2*sw**3',
                  order = {'NP':1,'QED':2})

GC_179 = Coupling(name = 'GC_179',
                  value = '8*complex(0,1)*FT0*gw**3*sw**3',
                  order = {'NP':1,'QED':3})

GC_180 = Coupling(name = 'GC_180',
                  value = '-4*complex(0,1)*FT1*gw**3*sw**3',
                  order = {'NP':1,'QED':3})

GC_181 = Coupling(name = 'GC_181',
                  value = '2*complex(0,1)*FT2*gw**3*sw**3',
                  order = {'NP':1,'QED':3})

GC_182 = Coupling(name = 'GC_182',
                  value = '-16*cw*complex(0,1)*FT0*gw**4*sw**3',
                  order = {'NP':1,'QED':4})

GC_183 = Coupling(name = 'GC_183',
                  value = '-16*cw*complex(0,1)*FT1*gw**4*sw**3',
                  order = {'NP':1,'QED':4})

GC_184 = Coupling(name = 'GC_184',
                  value = '-4*cw*complex(0,1)*FT2*gw**4*sw**3',
                  order = {'NP':1,'QED':4})

GC_185 = Coupling(name = 'GC_185',
                  value = '2*complex(0,1)*FT2*sw**4',
                  order = {'NP':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '-8*complex(0,1)*FT0*gw**2*sw**4',
                  order = {'NP':1,'QED':2})

GC_187 = Coupling(name = 'GC_187',
                  value = '-4*complex(0,1)*FT1*gw**2*sw**4',
                  order = {'NP':1,'QED':2})

GC_188 = Coupling(name = 'GC_188',
                  value = '-2*complex(0,1)*FT2*gw**2*sw**4',
                  order = {'NP':1,'QED':2})

GC_189 = Coupling(name = 'GC_189',
                  value = '16*complex(0,1)*FT0*gw**4*sw**4',
                  order = {'NP':1,'QED':4})

GC_190 = Coupling(name = 'GC_190',
                  value = '16*complex(0,1)*FT1*gw**4*sw**4',
                  order = {'NP':1,'QED':4})

GC_191 = Coupling(name = 'GC_191',
                  value = '8*complex(0,1)*FT2*gw**4*sw**4',
                  order = {'NP':1,'QED':4})

GC_192 = Coupling(name = 'GC_192',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '-2*cw*FM0*complex(0,1)*sw - cw*FM6*complex(0,1)*sw',
                  order = {'NP':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '-(cw*FM1*complex(0,1)*sw)/2. + (cw*FM7*complex(0,1)*sw)/4.',
                  order = {'NP':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '8*cw**3*complex(0,1)*FT0*sw + 8*cw**3*complex(0,1)*FT1*sw',
                  order = {'NP':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '2*FM0*complex(0,1)*gw*sw + FM6*complex(0,1)*gw*sw',
                  order = {'NP':1,'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '-(FM1*complex(0,1)*gw*sw)/2. + (FM7*complex(0,1)*gw*sw)/4.',
                  order = {'NP':1,'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '-4*cw*FM0*complex(0,1)*gw**2*sw - 2*cw*FM6*complex(0,1)*gw**2*sw',
                  order = {'NP':1,'QED':2})

GC_199 = Coupling(name = 'GC_199',
                  value = '-(cw*FM1*complex(0,1)*gw**2*sw)/2. + (cw*FM7*complex(0,1)*gw**2*sw)/4.',
                  order = {'NP':1,'QED':2})

GC_200 = Coupling(name = 'GC_200',
                  value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_201 = Coupling(name = 'GC_201',
                  value = '-2*FM0*complex(0,1)*sw**2 - FM6*complex(0,1)*sw**2',
                  order = {'NP':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '2*cw**2*ee**2*FM0*complex(0,1) + cw**2*ee**2*FM6*complex(0,1) + (cw**4*ee**2*FM0*complex(0,1))/sw**2 + (cw**4*ee**2*FM6*complex(0,1))/(2.*sw**2) + ee**2*FM0*complex(0,1)*sw**2 + (ee**2*FM6*complex(0,1)*sw**2)/2.',
                  order = {'NP':1,'QED':2})

GC_203 = Coupling(name = 'GC_203',
                  value = '2*ee**2*FM0*complex(0,1) + ee**2*FM6*complex(0,1) + (ee**2*FM0*complex(0,1)*sw**2)/cw**2 + (ee**2*FM6*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_204 = Coupling(name = 'GC_204',
                  value = '-(FM1*complex(0,1)*sw**2)/2. + (FM7*complex(0,1)*sw**2)/4.',
                  order = {'NP':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '(cw**2*ee**2*FM1*complex(0,1))/2. - (cw**2*ee**2*FM7*complex(0,1))/4. + (cw**4*ee**2*FM1*complex(0,1))/(4.*sw**2) - (cw**4*ee**2*FM7*complex(0,1))/(8.*sw**2) + (ee**2*FM1*complex(0,1)*sw**2)/4. - (ee**2*FM7*complex(0,1)*sw**2)/8.',
                  order = {'NP':1,'QED':2})

GC_206 = Coupling(name = 'GC_206',
                  value = '(ee**2*FM1*complex(0,1))/2. + (ee**2*FM1*complex(0,1)*sw**2)/(4.*cw**2) - (ee**2*FM7*complex(0,1)*sw**2)/(8.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_207 = Coupling(name = 'GC_207',
                  value = '-2*ee**2*complex(0,1)*FS0 - (cw**2*ee**2*complex(0,1)*FS0)/sw**2 - (ee**2*complex(0,1)*FS0*sw**2)/cw**2',
                  order = {'NP':1,'QED':2})

GC_208 = Coupling(name = 'GC_208',
                  value = '-2*ee**2*complex(0,1)*FS1 - (cw**2*ee**2*complex(0,1)*FS1)/sw**2 - (ee**2*complex(0,1)*FS1*sw**2)/cw**2',
                  order = {'NP':1,'QED':2})

GC_209 = Coupling(name = 'GC_209',
                  value = '8*cw**2*complex(0,1)*FT0*sw**2 + 8*cw**2*complex(0,1)*FT1*sw**2',
                  order = {'NP':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '-2*cw*ee**2*FM0*complex(0,1)*gw - cw*ee**2*FM6*complex(0,1)*gw - (cw**3*ee**2*FM0*complex(0,1)*gw)/sw**2 - (cw**3*ee**2*FM6*complex(0,1)*gw)/(2.*sw**2) - (ee**2*FM0*complex(0,1)*gw*sw**2)/cw - (ee**2*FM6*complex(0,1)*gw*sw**2)/(2.*cw)',
                  order = {'NP':1,'QED':3})

GC_211 = Coupling(name = 'GC_211',
                  value = '(cw*ee**2*FM7*complex(0,1)*gw)/8. + (ee**2*FM7*complex(0,1)*gw*sw**2)/(8.*cw)',
                  order = {'NP':1,'QED':3})

GC_212 = Coupling(name = 'GC_212',
                  value = '-(cw*ee**2*FM1*complex(0,1)*gw)/2. - (cw**3*ee**2*FM1*complex(0,1)*gw)/(4.*sw**2) - (ee**2*FM1*complex(0,1)*gw*sw**2)/(4.*cw) + (ee**2*FM7*complex(0,1)*gw*sw**2)/(8.*cw)',
                  order = {'NP':1,'QED':3})

GC_213 = Coupling(name = 'GC_213',
                  value = '2*FM0*complex(0,1)*gw**2*sw**2 + FM6*complex(0,1)*gw**2*sw**2',
                  order = {'NP':1,'QED':2})

GC_214 = Coupling(name = 'GC_214',
                  value = '2*ee**2*FM0*complex(0,1)*gw**2 + ee**2*FM6*complex(0,1)*gw**2 + (ee**2*FM0*complex(0,1)*gw**2*sw**2)/cw**2 + (ee**2*FM6*complex(0,1)*gw**2*sw**2)/(2.*cw**2)',
                  order = {'NP':1,'QED':4})

GC_215 = Coupling(name = 'GC_215',
                  value = 'FM1*complex(0,1)*gw**2*sw**2 - (FM7*complex(0,1)*gw**2*sw**2)/2.',
                  order = {'NP':1,'QED':2})

GC_216 = Coupling(name = 'GC_216',
                  value = '-(cw**2*ee*FM7*complex(0,1)*gw**2)/8. - (ee*FM7*complex(0,1)*gw**2*sw**2)/8.',
                  order = {'NP':1,'QED':3})

GC_217 = Coupling(name = 'GC_217',
                  value = '-2*cw**2*ee**2*FM0*complex(0,1)*gw**2 + cw**2*ee**2*FM1*complex(0,1)*gw**2 - cw**2*ee**2*FM6*complex(0,1)*gw**2 - (cw**2*ee**2*FM7*complex(0,1)*gw**2)/2. - (cw**4*ee**2*FM0*complex(0,1)*gw**2)/sw**2 + (cw**4*ee**2*FM1*complex(0,1)*gw**2)/(2.*sw**2) - (cw**4*ee**2*FM6*complex(0,1)*gw**2)/(2.*sw**2) - (cw**4*ee**2*FM7*complex(0,1)*gw**2)/(4.*sw**2) - ee**2*FM0*complex(0,1)*gw**2*sw**2 + (ee**2*FM1*complex(0,1)*gw**2*sw**2)/2. - (ee**2*FM6*complex(0,1)*gw**2*sw**2)/2. - (ee**2*FM7*complex(0,1)*gw**2*sw**2)/4.',
                  order = {'NP':1,'QED':4})

GC_218 = Coupling(name = 'GC_218',
                  value = 'ee**2*FM1*complex(0,1)*gw**2 + (ee**2*FM1*complex(0,1)*gw**2*sw**2)/(2.*cw**2) - (ee**2*FM7*complex(0,1)*gw**2*sw**2)/(4.*cw**2)',
                  order = {'NP':1,'QED':4})

GC_219 = Coupling(name = 'GC_219',
                  value = '(cw**3*ee**2*FM0*complex(0,1))/sw + (cw**3*ee**2*FM6*complex(0,1))/(2.*sw) + 2*cw*ee**2*FM0*complex(0,1)*sw + cw*ee**2*FM6*complex(0,1)*sw + (ee**2*FM0*complex(0,1)*sw**3)/cw + (ee**2*FM6*complex(0,1)*sw**3)/(2.*cw)',
                  order = {'NP':1,'QED':2})

GC_220 = Coupling(name = 'GC_220',
                  value = '(cw**3*ee**2*FM1*complex(0,1))/(4.*sw) - (cw**3*ee**2*FM7*complex(0,1))/(8.*sw) + (cw*ee**2*FM1*complex(0,1)*sw)/2. - (cw*ee**2*FM7*complex(0,1)*sw)/4. + (ee**2*FM1*complex(0,1)*sw**3)/(4.*cw) - (ee**2*FM7*complex(0,1)*sw**3)/(8.*cw)',
                  order = {'NP':1,'QED':2})

GC_221 = Coupling(name = 'GC_221',
                  value = '8*cw*complex(0,1)*FT0*sw**3 + 8*cw*complex(0,1)*FT1*sw**3',
                  order = {'NP':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '-((cw**2*ee**2*FM0*complex(0,1)*gw)/sw) - (cw**2*ee**2*FM6*complex(0,1)*gw)/(2.*sw) - 2*ee**2*FM0*complex(0,1)*gw*sw - ee**2*FM6*complex(0,1)*gw*sw - (ee**2*FM0*complex(0,1)*gw*sw**3)/cw**2 - (ee**2*FM6*complex(0,1)*gw*sw**3)/(2.*cw**2)',
                  order = {'NP':1,'QED':3})

GC_223 = Coupling(name = 'GC_223',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*gw)/(4.*sw) + (ee**2*FM1*complex(0,1)*gw*sw)/2. + (ee**2*FM1*complex(0,1)*gw*sw**3)/(4.*cw**2) - (ee**2*FM7*complex(0,1)*gw*sw**3)/(8.*cw**2)',
                  order = {'NP':1,'QED':3})

GC_224 = Coupling(name = 'GC_224',
                  value = '-(cw*ee*FM7*complex(0,1)*gw**2*sw)/8. - (ee*FM7*complex(0,1)*gw**2*sw**3)/(8.*cw)',
                  order = {'NP':1,'QED':3})

GC_225 = Coupling(name = 'GC_225',
                  value = '(2*cw**3*ee**2*FM0*complex(0,1)*gw**2)/sw - (cw**3*ee**2*FM1*complex(0,1)*gw**2)/sw + (cw**3*ee**2*FM6*complex(0,1)*gw**2)/sw + (cw**3*ee**2*FM7*complex(0,1)*gw**2)/(2.*sw) + 4*cw*ee**2*FM0*complex(0,1)*gw**2*sw - 2*cw*ee**2*FM1*complex(0,1)*gw**2*sw + 2*cw*ee**2*FM6*complex(0,1)*gw**2*sw + cw*ee**2*FM7*complex(0,1)*gw**2*sw + (2*ee**2*FM0*complex(0,1)*gw**2*sw**3)/cw - (ee**2*FM1*complex(0,1)*gw**2*sw**3)/cw + (ee**2*FM6*complex(0,1)*gw**2*sw**3)/cw + (ee**2*FM7*complex(0,1)*gw**2*sw**3)/(2.*cw)',
                  order = {'NP':1,'QED':4})

GC_226 = Coupling(name = 'GC_226',
                  value = 'cw**2*ee**2*FM0*complex(0,1) + (cw**2*ee**2*FM6*complex(0,1))/2. + 2*ee**2*FM0*complex(0,1)*sw**2 + ee**2*FM6*complex(0,1)*sw**2 + (ee**2*FM0*complex(0,1)*sw**4)/cw**2 + (ee**2*FM6*complex(0,1)*sw**4)/(2.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_227 = Coupling(name = 'GC_227',
                  value = '(cw**2*ee**2*FM1*complex(0,1))/4. - (cw**2*ee**2*FM7*complex(0,1))/8. + (ee**2*FM1*complex(0,1)*sw**2)/2. - (ee**2*FM7*complex(0,1)*sw**2)/4. + (ee**2*FM1*complex(0,1)*sw**4)/(4.*cw**2) - (ee**2*FM7*complex(0,1)*sw**4)/(8.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_228 = Coupling(name = 'GC_228',
                  value = '18*ee**4*complex(0,1)*FS0 + 18*ee**4*complex(0,1)*FS1 + (3*cw**4*ee**4*complex(0,1)*FS0)/sw**4 + (3*cw**4*ee**4*complex(0,1)*FS1)/sw**4 + (12*cw**2*ee**4*complex(0,1)*FS0)/sw**2 + (12*cw**2*ee**4*complex(0,1)*FS1)/sw**2 + (12*ee**4*complex(0,1)*FS0*sw**2)/cw**2 + (12*ee**4*complex(0,1)*FS1*sw**2)/cw**2 + (3*ee**4*complex(0,1)*FS0*sw**4)/cw**4 + (3*ee**4*complex(0,1)*FS1*sw**4)/cw**4',
                  order = {'NP':1,'QED':4})

GC_229 = Coupling(name = 'GC_229',
                  value = '8*complex(0,1)*FT0*sw**4 + 8*complex(0,1)*FT1*sw**4',
                  order = {'NP':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '-(cw**2*ee**2*FM0*complex(0,1)*gw**2) - (cw**2*ee**2*FM6*complex(0,1)*gw**2)/2. - 2*ee**2*FM0*complex(0,1)*gw**2*sw**2 - ee**2*FM6*complex(0,1)*gw**2*sw**2 - (ee**2*FM0*complex(0,1)*gw**2*sw**4)/cw**2 - (ee**2*FM6*complex(0,1)*gw**2*sw**4)/(2.*cw**2)',
                  order = {'NP':1,'QED':4})

GC_231 = Coupling(name = 'GC_231',
                  value = '-(cw**2*ee**2*FM1*complex(0,1)*gw**2)/2. + (cw**2*ee**2*FM7*complex(0,1)*gw**2)/4. - ee**2*FM1*complex(0,1)*gw**2*sw**2 + (ee**2*FM7*complex(0,1)*gw**2*sw**2)/2. - (ee**2*FM1*complex(0,1)*gw**2*sw**4)/(2.*cw**2) + (ee**2*FM7*complex(0,1)*gw**2*sw**4)/(4.*cw**2)',
                  order = {'NP':1,'QED':4})

GC_232 = Coupling(name = 'GC_232',
                  value = '-(ee*FM7*complex(0,1)*v)/8.',
                  order = {'NP':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '-(ee**2*FM7*complex(0,1)*v)/4.',
                  order = {'NP':1,'QED':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '(cw*ee*FM7*complex(0,1)*gw*v)/8.',
                  order = {'NP':1,'QED':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '(ee**2*FM7*complex(0,1)*gw*v)/(8.*cw)',
                  order = {'NP':1,'QED':2})

GC_236 = Coupling(name = 'GC_236',
                  value = '(cw*ee**2*FM7*complex(0,1)*gw*v)/2.',
                  order = {'NP':1,'QED':2})

GC_237 = Coupling(name = 'GC_237',
                  value = 'ee**2*FM1*complex(0,1)*gw**2*v',
                  order = {'NP':1,'QED':3})

GC_238 = Coupling(name = 'GC_238',
                  value = '-(ee**2*FM7*complex(0,1)*gw**2*v)',
                  order = {'NP':1,'QED':3})

GC_239 = Coupling(name = 'GC_239',
                  value = '(-3*ee**2*FM7*complex(0,1)*gw**2*v)/2.',
                  order = {'NP':1,'QED':3})

GC_240 = Coupling(name = 'GC_240',
                  value = '-6*complex(0,1)*lam*v',
                  order = {'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '(6*ee**4*complex(0,1)*FS0*v)/sw**4',
                  order = {'NP':1,'QED':3})

GC_242 = Coupling(name = 'GC_242',
                  value = '(3*ee**4*complex(0,1)*FS1*v)/sw**4',
                  order = {'NP':1,'QED':3})

GC_243 = Coupling(name = 'GC_243',
                  value = '(ee**2*complex(0,1)*v)/(2.*sw**2)',
                  order = {'QED':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '-(ee**2*FM1*complex(0,1)*v)/(4.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_245 = Coupling(name = 'GC_245',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*v)/(4.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '(ee**2*FM7*complex(0,1)*v)/(4.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_247 = Coupling(name = 'GC_247',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*v)/(8.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_248 = Coupling(name = 'GC_248',
                  value = '-(ee**2*complex(0,1)*FS0*v)/(2.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_249 = Coupling(name = 'GC_249',
                  value = '-((ee**2*complex(0,1)*FS1*v)/sw**2)',
                  order = {'NP':1,'QED':1})

GC_250 = Coupling(name = 'GC_250',
                  value = '(cw*ee**2*FM1*complex(0,1)*gw*v)/(4.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_251 = Coupling(name = 'GC_251',
                  value = '(cw*ee**2*FM7*complex(0,1)*gw*v)/(8.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_252 = Coupling(name = 'GC_252',
                  value = '(3*cw**3*ee**2*FM7*complex(0,1)*gw*v)/(8.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_253 = Coupling(name = 'GC_253',
                  value = '(3*cw**2*ee**2*FM1*complex(0,1)*gw**2*v)/(2.*sw**2)',
                  order = {'NP':1,'QED':3})

GC_254 = Coupling(name = 'GC_254',
                  value = '(-9*cw**2*ee**2*FM7*complex(0,1)*gw**2*v)/(4.*sw**2)',
                  order = {'NP':1,'QED':3})

GC_255 = Coupling(name = 'GC_255',
                  value = '-(cw*ee**2*FM1*complex(0,1)*v)/(4.*sw)',
                  order = {'NP':1,'QED':1})

GC_256 = Coupling(name = 'GC_256',
                  value = '-(cw*ee*FM7*complex(0,1)*v)/(8.*sw)',
                  order = {'NP':1})

GC_257 = Coupling(name = 'GC_257',
                  value = '(cw*ee**2*FM7*complex(0,1)*v)/(8.*sw)',
                  order = {'NP':1,'QED':1})

GC_258 = Coupling(name = 'GC_258',
                  value = '-(ee**2*FM1*complex(0,1)*gw*v)/(4.*sw)',
                  order = {'NP':1,'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '(ee*FM7*complex(0,1)*gw*v)/(8.*sw)',
                  order = {'NP':1,'QED':1})

GC_260 = Coupling(name = 'GC_260',
                  value = '-(cw**2*ee*FM7*complex(0,1)*gw*v)/(8.*sw)',
                  order = {'NP':1,'QED':1})

GC_261 = Coupling(name = 'GC_261',
                  value = '(ee**2*FM7*complex(0,1)*gw*v)/(4.*sw)',
                  order = {'NP':1,'QED':2})

GC_262 = Coupling(name = 'GC_262',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*gw*v)/(8.*sw)',
                  order = {'NP':1,'QED':2})

GC_263 = Coupling(name = 'GC_263',
                  value = '-((cw*ee**2*FM1*complex(0,1)*gw**2*v)/sw)',
                  order = {'NP':1,'QED':3})

GC_264 = Coupling(name = 'GC_264',
                  value = '-(cw*ee**2*FM7*complex(0,1)*gw**2*v)/(2.*sw)',
                  order = {'NP':1,'QED':3})

GC_265 = Coupling(name = 'GC_265',
                  value = '-(ee*FM7*complex(0,1)*sw*v)/(8.*cw)',
                  order = {'NP':1})

GC_266 = Coupling(name = 'GC_266',
                  value = '(ee**2*FM7*complex(0,1)*sw*v)/(8.*cw)',
                  order = {'NP':1,'QED':1})

GC_267 = Coupling(name = 'GC_267',
                  value = '-(ee*FM7*complex(0,1)*gw*sw*v)/8.',
                  order = {'NP':1,'QED':1})

GC_268 = Coupling(name = 'GC_268',
                  value = '-(ee**2*FM7*complex(0,1)*gw*sw*v)/4.',
                  order = {'NP':1,'QED':2})

GC_269 = Coupling(name = 'GC_269',
                  value = '-(ee**2*FM7*complex(0,1)*gw**2*sw*v)/(2.*cw)',
                  order = {'NP':1,'QED':3})

GC_270 = Coupling(name = 'GC_270',
                  value = '(ee*FM7*complex(0,1)*gw*sw**2*v)/(8.*cw)',
                  order = {'NP':1,'QED':1})

GC_271 = Coupling(name = 'GC_271',
                  value = '-(ee**2*FM7*complex(0,1)*v**2)/8.',
                  order = {'NP':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '(ee**2*FM7*complex(0,1)*gw*v**2)/(16.*cw)',
                  order = {'NP':1,'QED':1})

GC_273 = Coupling(name = 'GC_273',
                  value = '(cw*ee**2*FM7*complex(0,1)*gw*v**2)/4.',
                  order = {'NP':1,'QED':1})

GC_274 = Coupling(name = 'GC_274',
                  value = '(ee**2*FM1*complex(0,1)*gw**2*v**2)/2.',
                  order = {'NP':1,'QED':2})

GC_275 = Coupling(name = 'GC_275',
                  value = '-(ee**2*FM7*complex(0,1)*gw**2*v**2)/2.',
                  order = {'NP':1,'QED':2})

GC_276 = Coupling(name = 'GC_276',
                  value = '(-3*ee**2*FM7*complex(0,1)*gw**2*v**2)/4.',
                  order = {'NP':1,'QED':2})

GC_277 = Coupling(name = 'GC_277',
                  value = '(3*ee**4*complex(0,1)*FS0*v**2)/sw**4',
                  order = {'NP':1,'QED':2})

GC_278 = Coupling(name = 'GC_278',
                  value = '(3*ee**4*complex(0,1)*FS1*v**2)/(2.*sw**4)',
                  order = {'NP':1,'QED':2})

GC_279 = Coupling(name = 'GC_279',
                  value = '-(ee**2*FM1*complex(0,1)*v**2)/(8.*sw**2)',
                  order = {'NP':1})

GC_280 = Coupling(name = 'GC_280',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*v**2)/(8.*sw**2)',
                  order = {'NP':1})

GC_281 = Coupling(name = 'GC_281',
                  value = '(ee**2*FM7*complex(0,1)*v**2)/(8.*sw**2)',
                  order = {'NP':1})

GC_282 = Coupling(name = 'GC_282',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*v**2)/(16.*sw**2)',
                  order = {'NP':1})

GC_283 = Coupling(name = 'GC_283',
                  value = '-(ee**2*complex(0,1)*FS0*v**2)/(4.*sw**2)',
                  order = {'NP':1})

GC_284 = Coupling(name = 'GC_284',
                  value = '-(ee**2*complex(0,1)*FS1*v**2)/(2.*sw**2)',
                  order = {'NP':1})

GC_285 = Coupling(name = 'GC_285',
                  value = '(cw*ee**2*FM1*complex(0,1)*gw*v**2)/(8.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_286 = Coupling(name = 'GC_286',
                  value = '(cw*ee**2*FM7*complex(0,1)*gw*v**2)/(16.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_287 = Coupling(name = 'GC_287',
                  value = '(3*cw**3*ee**2*FM7*complex(0,1)*gw*v**2)/(16.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_288 = Coupling(name = 'GC_288',
                  value = '(3*cw**2*ee**2*FM1*complex(0,1)*gw**2*v**2)/(4.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_289 = Coupling(name = 'GC_289',
                  value = '(-9*cw**2*ee**2*FM7*complex(0,1)*gw**2*v**2)/(8.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_290 = Coupling(name = 'GC_290',
                  value = '-(cw*ee**2*FM1*complex(0,1)*v**2)/(8.*sw)',
                  order = {'NP':1})

GC_291 = Coupling(name = 'GC_291',
                  value = '(cw*ee**2*FM7*complex(0,1)*v**2)/(16.*sw)',
                  order = {'NP':1})

GC_292 = Coupling(name = 'GC_292',
                  value = '-(ee**2*FM1*complex(0,1)*gw*v**2)/(8.*sw)',
                  order = {'NP':1,'QED':1})

GC_293 = Coupling(name = 'GC_293',
                  value = '(ee**2*FM7*complex(0,1)*gw*v**2)/(8.*sw)',
                  order = {'NP':1,'QED':1})

GC_294 = Coupling(name = 'GC_294',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*gw*v**2)/(16.*sw)',
                  order = {'NP':1,'QED':1})

GC_295 = Coupling(name = 'GC_295',
                  value = '-(cw*ee**2*FM1*complex(0,1)*gw**2*v**2)/(2.*sw)',
                  order = {'NP':1,'QED':2})

GC_296 = Coupling(name = 'GC_296',
                  value = '-(cw*ee**2*FM7*complex(0,1)*gw**2*v**2)/(4.*sw)',
                  order = {'NP':1,'QED':2})

GC_297 = Coupling(name = 'GC_297',
                  value = '(ee**2*FM7*complex(0,1)*sw*v**2)/(16.*cw)',
                  order = {'NP':1})

GC_298 = Coupling(name = 'GC_298',
                  value = '-(ee**2*FM7*complex(0,1)*gw*sw*v**2)/8.',
                  order = {'NP':1,'QED':1})

GC_299 = Coupling(name = 'GC_299',
                  value = '-(ee**2*FM7*complex(0,1)*gw**2*sw*v**2)/(4.*cw)',
                  order = {'NP':1,'QED':2})

GC_300 = Coupling(name = 'GC_300',
                  value = '(ee**4*complex(0,1)*FS0*v**3)/sw**4',
                  order = {'NP':1,'QED':1})

GC_301 = Coupling(name = 'GC_301',
                  value = '(ee**4*complex(0,1)*FS1*v**3)/(2.*sw**4)',
                  order = {'NP':1,'QED':1})

GC_302 = Coupling(name = 'GC_302',
                  value = '(ee**4*complex(0,1)*FS0*v**4)/(4.*sw**4)',
                  order = {'NP':1})

GC_303 = Coupling(name = 'GC_303',
                  value = '(ee**4*complex(0,1)*FS1*v**4)/(8.*sw**4)',
                  order = {'NP':1})

GC_304 = Coupling(name = 'GC_304',
                  value = 'ee**2*FM0*complex(0,1)*v + (ee**2*FM6*complex(0,1)*v)/2.',
                  order = {'NP':1,'QED':1})

GC_305 = Coupling(name = 'GC_305',
                  value = '(ee**2*FM1*complex(0,1)*v)/4. - (ee**2*FM7*complex(0,1)*v)/8.',
                  order = {'NP':1,'QED':1})

GC_306 = Coupling(name = 'GC_306',
                  value = '-(ee**2*FM0*complex(0,1)*gw**2*v) - (ee**2*FM6*complex(0,1)*gw**2*v)/2.',
                  order = {'NP':1,'QED':3})

GC_307 = Coupling(name = 'GC_307',
                  value = '(ee**2*FM0*complex(0,1)*v)/sw**2 + (ee**2*FM6*complex(0,1)*v)/(2.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_308 = Coupling(name = 'GC_308',
                  value = '(cw**2*ee**2*FM0*complex(0,1)*v)/sw**2 + (cw**2*ee**2*FM6*complex(0,1)*v)/(2.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_309 = Coupling(name = 'GC_309',
                  value = '(3*ee**4*complex(0,1)*FS0*v)/(2.*cw**2) + (3*cw**2*ee**4*complex(0,1)*FS0*v)/(2.*sw**4) + (3*ee**4*complex(0,1)*FS0*v)/sw**2',
                  order = {'NP':1,'QED':3})

GC_310 = Coupling(name = 'GC_310',
                  value = '(3*ee**4*complex(0,1)*FS1*v)/cw**2 + (3*cw**2*ee**4*complex(0,1)*FS1*v)/sw**4 + (6*ee**4*complex(0,1)*FS1*v)/sw**2',
                  order = {'NP':1,'QED':3})

GC_311 = Coupling(name = 'GC_311',
                  value = '-((cw*ee**2*FM0*complex(0,1)*gw*v)/sw**2) - (cw*ee**2*FM6*complex(0,1)*gw*v)/(2.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_312 = Coupling(name = 'GC_312',
                  value = '-((cw**2*ee**2*FM0*complex(0,1)*gw**2*v)/sw**2) - (cw**2*ee**2*FM6*complex(0,1)*gw**2*v)/(2.*sw**2)',
                  order = {'NP':1,'QED':3})

GC_313 = Coupling(name = 'GC_313',
                  value = '(3*ee**2*FM0*complex(0,1)*gw**2*v)/sw**2 - (3*ee**2*FM1*complex(0,1)*gw**2*v)/(2.*sw**2) + (3*ee**2*FM6*complex(0,1)*gw**2*v)/(2.*sw**2) + (3*ee**2*FM7*complex(0,1)*gw**2*v)/(4.*sw**2)',
                  order = {'NP':1,'QED':3})

GC_314 = Coupling(name = 'GC_314',
                  value = '(cw*ee**2*FM0*complex(0,1)*v)/sw + (cw*ee**2*FM6*complex(0,1)*v)/(2.*sw)',
                  order = {'NP':1,'QED':1})

GC_315 = Coupling(name = 'GC_315',
                  value = '(-3*cw*ee**3*complex(0,1)*FS0*v)/(4.*sw**3) - (3*ee**3*complex(0,1)*FS0*v)/(4.*cw*sw)',
                  order = {'NP':1,'QED':2})

GC_316 = Coupling(name = 'GC_316',
                  value = '-((ee**2*FM0*complex(0,1)*gw*v)/sw) - (ee**2*FM6*complex(0,1)*gw*v)/(2.*sw)',
                  order = {'NP':1,'QED':2})

GC_317 = Coupling(name = 'GC_317',
                  value = '(4*cw*ee**2*FM0*complex(0,1)*gw**2*v)/sw + (2*cw*ee**2*FM6*complex(0,1)*gw**2*v)/sw',
                  order = {'NP':1,'QED':3})

GC_318 = Coupling(name = 'GC_318',
                  value = 'ee**2*complex(0,1)*v + (cw**2*ee**2*complex(0,1)*v)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*v)/(2.*cw**2)',
                  order = {'QED':1})

GC_319 = Coupling(name = 'GC_319',
                  value = '2*cw**2*ee**2*FM0*complex(0,1)*v + cw**2*ee**2*FM6*complex(0,1)*v + (cw**4*ee**2*FM0*complex(0,1)*v)/sw**2 + (cw**4*ee**2*FM6*complex(0,1)*v)/(2.*sw**2) + ee**2*FM0*complex(0,1)*sw**2*v + (ee**2*FM6*complex(0,1)*sw**2*v)/2.',
                  order = {'NP':1,'QED':1})

GC_320 = Coupling(name = 'GC_320',
                  value = '2*ee**2*FM0*complex(0,1)*v + ee**2*FM6*complex(0,1)*v + (ee**2*FM0*complex(0,1)*sw**2*v)/cw**2 + (ee**2*FM6*complex(0,1)*sw**2*v)/(2.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_321 = Coupling(name = 'GC_321',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*v)/2. - (cw**2*ee**2*FM7*complex(0,1)*v)/4. + (cw**4*ee**2*FM1*complex(0,1)*v)/(4.*sw**2) - (cw**4*ee**2*FM7*complex(0,1)*v)/(8.*sw**2) + (ee**2*FM1*complex(0,1)*sw**2*v)/4. - (ee**2*FM7*complex(0,1)*sw**2*v)/8.',
                  order = {'NP':1,'QED':1})

GC_322 = Coupling(name = 'GC_322',
                  value = '(ee**2*FM1*complex(0,1)*v)/2. + (ee**2*FM1*complex(0,1)*sw**2*v)/(4.*cw**2) - (ee**2*FM7*complex(0,1)*sw**2*v)/(8.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_323 = Coupling(name = 'GC_323',
                  value = '-2*ee**2*complex(0,1)*FS0*v - (cw**2*ee**2*complex(0,1)*FS0*v)/sw**2 - (ee**2*complex(0,1)*FS0*sw**2*v)/cw**2',
                  order = {'NP':1,'QED':1})

GC_324 = Coupling(name = 'GC_324',
                  value = '-2*ee**2*complex(0,1)*FS1*v - (cw**2*ee**2*complex(0,1)*FS1*v)/sw**2 - (ee**2*complex(0,1)*FS1*sw**2*v)/cw**2',
                  order = {'NP':1,'QED':1})

GC_325 = Coupling(name = 'GC_325',
                  value = '-2*cw*ee**2*FM0*complex(0,1)*gw*v - cw*ee**2*FM6*complex(0,1)*gw*v - (cw**3*ee**2*FM0*complex(0,1)*gw*v)/sw**2 - (cw**3*ee**2*FM6*complex(0,1)*gw*v)/(2.*sw**2) - (ee**2*FM0*complex(0,1)*gw*sw**2*v)/cw - (ee**2*FM6*complex(0,1)*gw*sw**2*v)/(2.*cw)',
                  order = {'NP':1,'QED':2})

GC_326 = Coupling(name = 'GC_326',
                  value = '(cw*ee**2*FM7*complex(0,1)*gw*v)/8. + (ee**2*FM7*complex(0,1)*gw*sw**2*v)/(8.*cw)',
                  order = {'NP':1,'QED':2})

GC_327 = Coupling(name = 'GC_327',
                  value = '-(cw*ee**2*FM1*complex(0,1)*gw*v)/2. - (cw**3*ee**2*FM1*complex(0,1)*gw*v)/(4.*sw**2) - (ee**2*FM1*complex(0,1)*gw*sw**2*v)/(4.*cw) + (ee**2*FM7*complex(0,1)*gw*sw**2*v)/(8.*cw)',
                  order = {'NP':1,'QED':2})

GC_328 = Coupling(name = 'GC_328',
                  value = '2*ee**2*FM0*complex(0,1)*gw**2*v + ee**2*FM6*complex(0,1)*gw**2*v + (ee**2*FM0*complex(0,1)*gw**2*sw**2*v)/cw**2 + (ee**2*FM6*complex(0,1)*gw**2*sw**2*v)/(2.*cw**2)',
                  order = {'NP':1,'QED':3})

GC_329 = Coupling(name = 'GC_329',
                  value = '-(cw**2*ee*FM7*complex(0,1)*gw**2*v)/8. - (ee*FM7*complex(0,1)*gw**2*sw**2*v)/8.',
                  order = {'NP':1,'QED':2})

GC_330 = Coupling(name = 'GC_330',
                  value = '-2*cw**2*ee**2*FM0*complex(0,1)*gw**2*v + cw**2*ee**2*FM1*complex(0,1)*gw**2*v - cw**2*ee**2*FM6*complex(0,1)*gw**2*v - (cw**2*ee**2*FM7*complex(0,1)*gw**2*v)/2. - (cw**4*ee**2*FM0*complex(0,1)*gw**2*v)/sw**2 + (cw**4*ee**2*FM1*complex(0,1)*gw**2*v)/(2.*sw**2) - (cw**4*ee**2*FM6*complex(0,1)*gw**2*v)/(2.*sw**2) - (cw**4*ee**2*FM7*complex(0,1)*gw**2*v)/(4.*sw**2) - ee**2*FM0*complex(0,1)*gw**2*sw**2*v + (ee**2*FM1*complex(0,1)*gw**2*sw**2*v)/2. - (ee**2*FM6*complex(0,1)*gw**2*sw**2*v)/2. - (ee**2*FM7*complex(0,1)*gw**2*sw**2*v)/4.',
                  order = {'NP':1,'QED':3})

GC_331 = Coupling(name = 'GC_331',
                  value = 'ee**2*FM1*complex(0,1)*gw**2*v + (ee**2*FM1*complex(0,1)*gw**2*sw**2*v)/(2.*cw**2) - (ee**2*FM7*complex(0,1)*gw**2*sw**2*v)/(4.*cw**2)',
                  order = {'NP':1,'QED':3})

GC_332 = Coupling(name = 'GC_332',
                  value = '(cw**3*ee**2*FM0*complex(0,1)*v)/sw + (cw**3*ee**2*FM6*complex(0,1)*v)/(2.*sw) + 2*cw*ee**2*FM0*complex(0,1)*sw*v + cw*ee**2*FM6*complex(0,1)*sw*v + (ee**2*FM0*complex(0,1)*sw**3*v)/cw + (ee**2*FM6*complex(0,1)*sw**3*v)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_333 = Coupling(name = 'GC_333',
                  value = '(cw**3*ee**2*FM1*complex(0,1)*v)/(4.*sw) - (cw**3*ee**2*FM7*complex(0,1)*v)/(8.*sw) + (cw*ee**2*FM1*complex(0,1)*sw*v)/2. - (cw*ee**2*FM7*complex(0,1)*sw*v)/4. + (ee**2*FM1*complex(0,1)*sw**3*v)/(4.*cw) - (ee**2*FM7*complex(0,1)*sw**3*v)/(8.*cw)',
                  order = {'NP':1,'QED':1})

GC_334 = Coupling(name = 'GC_334',
                  value = '-((cw**2*ee**2*FM0*complex(0,1)*gw*v)/sw) - (cw**2*ee**2*FM6*complex(0,1)*gw*v)/(2.*sw) - 2*ee**2*FM0*complex(0,1)*gw*sw*v - ee**2*FM6*complex(0,1)*gw*sw*v - (ee**2*FM0*complex(0,1)*gw*sw**3*v)/cw**2 - (ee**2*FM6*complex(0,1)*gw*sw**3*v)/(2.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_335 = Coupling(name = 'GC_335',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*gw*v)/(4.*sw) + (ee**2*FM1*complex(0,1)*gw*sw*v)/2. + (ee**2*FM1*complex(0,1)*gw*sw**3*v)/(4.*cw**2) - (ee**2*FM7*complex(0,1)*gw*sw**3*v)/(8.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_336 = Coupling(name = 'GC_336',
                  value = '-(cw*ee*FM7*complex(0,1)*gw**2*sw*v)/8. - (ee*FM7*complex(0,1)*gw**2*sw**3*v)/(8.*cw)',
                  order = {'NP':1,'QED':2})

GC_337 = Coupling(name = 'GC_337',
                  value = '(2*cw**3*ee**2*FM0*complex(0,1)*gw**2*v)/sw - (cw**3*ee**2*FM1*complex(0,1)*gw**2*v)/sw + (cw**3*ee**2*FM6*complex(0,1)*gw**2*v)/sw + (cw**3*ee**2*FM7*complex(0,1)*gw**2*v)/(2.*sw) + 4*cw*ee**2*FM0*complex(0,1)*gw**2*sw*v - 2*cw*ee**2*FM1*complex(0,1)*gw**2*sw*v + 2*cw*ee**2*FM6*complex(0,1)*gw**2*sw*v + cw*ee**2*FM7*complex(0,1)*gw**2*sw*v + (2*ee**2*FM0*complex(0,1)*gw**2*sw**3*v)/cw - (ee**2*FM1*complex(0,1)*gw**2*sw**3*v)/cw + (ee**2*FM6*complex(0,1)*gw**2*sw**3*v)/cw + (ee**2*FM7*complex(0,1)*gw**2*sw**3*v)/(2.*cw)',
                  order = {'NP':1,'QED':3})

GC_338 = Coupling(name = 'GC_338',
                  value = 'cw**2*ee**2*FM0*complex(0,1)*v + (cw**2*ee**2*FM6*complex(0,1)*v)/2. + 2*ee**2*FM0*complex(0,1)*sw**2*v + ee**2*FM6*complex(0,1)*sw**2*v + (ee**2*FM0*complex(0,1)*sw**4*v)/cw**2 + (ee**2*FM6*complex(0,1)*sw**4*v)/(2.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_339 = Coupling(name = 'GC_339',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*v)/4. - (cw**2*ee**2*FM7*complex(0,1)*v)/8. + (ee**2*FM1*complex(0,1)*sw**2*v)/2. - (ee**2*FM7*complex(0,1)*sw**2*v)/4. + (ee**2*FM1*complex(0,1)*sw**4*v)/(4.*cw**2) - (ee**2*FM7*complex(0,1)*sw**4*v)/(8.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_340 = Coupling(name = 'GC_340',
                  value = '18*ee**4*complex(0,1)*FS0*v + 18*ee**4*complex(0,1)*FS1*v + (3*cw**4*ee**4*complex(0,1)*FS0*v)/sw**4 + (3*cw**4*ee**4*complex(0,1)*FS1*v)/sw**4 + (12*cw**2*ee**4*complex(0,1)*FS0*v)/sw**2 + (12*cw**2*ee**4*complex(0,1)*FS1*v)/sw**2 + (12*ee**4*complex(0,1)*FS0*sw**2*v)/cw**2 + (12*ee**4*complex(0,1)*FS1*sw**2*v)/cw**2 + (3*ee**4*complex(0,1)*FS0*sw**4*v)/cw**4 + (3*ee**4*complex(0,1)*FS1*sw**4*v)/cw**4',
                  order = {'NP':1,'QED':3})

GC_341 = Coupling(name = 'GC_341',
                  value = '-(cw**2*ee**2*FM0*complex(0,1)*gw**2*v) - (cw**2*ee**2*FM6*complex(0,1)*gw**2*v)/2. - 2*ee**2*FM0*complex(0,1)*gw**2*sw**2*v - ee**2*FM6*complex(0,1)*gw**2*sw**2*v - (ee**2*FM0*complex(0,1)*gw**2*sw**4*v)/cw**2 - (ee**2*FM6*complex(0,1)*gw**2*sw**4*v)/(2.*cw**2)',
                  order = {'NP':1,'QED':3})

GC_342 = Coupling(name = 'GC_342',
                  value = '-(cw**2*ee**2*FM1*complex(0,1)*gw**2*v)/2. + (cw**2*ee**2*FM7*complex(0,1)*gw**2*v)/4. - ee**2*FM1*complex(0,1)*gw**2*sw**2*v + (ee**2*FM7*complex(0,1)*gw**2*sw**2*v)/2. - (ee**2*FM1*complex(0,1)*gw**2*sw**4*v)/(2.*cw**2) + (ee**2*FM7*complex(0,1)*gw**2*sw**4*v)/(4.*cw**2)',
                  order = {'NP':1,'QED':3})

GC_343 = Coupling(name = 'GC_343',
                  value = '(ee**2*FM0*complex(0,1)*v**2)/2. + (ee**2*FM6*complex(0,1)*v**2)/4.',
                  order = {'NP':1})

GC_344 = Coupling(name = 'GC_344',
                  value = '(ee**2*FM1*complex(0,1)*v**2)/8. - (ee**2*FM7*complex(0,1)*v**2)/16.',
                  order = {'NP':1})

GC_345 = Coupling(name = 'GC_345',
                  value = '-(ee**2*FM0*complex(0,1)*gw**2*v**2)/2. - (ee**2*FM6*complex(0,1)*gw**2*v**2)/4.',
                  order = {'NP':1,'QED':2})

GC_346 = Coupling(name = 'GC_346',
                  value = '(ee**2*FM0*complex(0,1)*v**2)/(2.*sw**2) + (ee**2*FM6*complex(0,1)*v**2)/(4.*sw**2)',
                  order = {'NP':1})

GC_347 = Coupling(name = 'GC_347',
                  value = '(cw**2*ee**2*FM0*complex(0,1)*v**2)/(2.*sw**2) + (cw**2*ee**2*FM6*complex(0,1)*v**2)/(4.*sw**2)',
                  order = {'NP':1})

GC_348 = Coupling(name = 'GC_348',
                  value = '(3*ee**4*complex(0,1)*FS0*v**2)/(4.*cw**2) + (3*cw**2*ee**4*complex(0,1)*FS0*v**2)/(4.*sw**4) + (3*ee**4*complex(0,1)*FS0*v**2)/(2.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_349 = Coupling(name = 'GC_349',
                  value = '(3*ee**4*complex(0,1)*FS1*v**2)/(2.*cw**2) + (3*cw**2*ee**4*complex(0,1)*FS1*v**2)/(2.*sw**4) + (3*ee**4*complex(0,1)*FS1*v**2)/sw**2',
                  order = {'NP':1,'QED':2})

GC_350 = Coupling(name = 'GC_350',
                  value = '-(cw*ee**2*FM0*complex(0,1)*gw*v**2)/(2.*sw**2) - (cw*ee**2*FM6*complex(0,1)*gw*v**2)/(4.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_351 = Coupling(name = 'GC_351',
                  value = '-(cw**2*ee**2*FM0*complex(0,1)*gw**2*v**2)/(2.*sw**2) - (cw**2*ee**2*FM6*complex(0,1)*gw**2*v**2)/(4.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_352 = Coupling(name = 'GC_352',
                  value = '(3*ee**2*FM0*complex(0,1)*gw**2*v**2)/(2.*sw**2) - (3*ee**2*FM1*complex(0,1)*gw**2*v**2)/(4.*sw**2) + (3*ee**2*FM6*complex(0,1)*gw**2*v**2)/(4.*sw**2) + (3*ee**2*FM7*complex(0,1)*gw**2*v**2)/(8.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_353 = Coupling(name = 'GC_353',
                  value = '(cw*ee**2*FM0*complex(0,1)*v**2)/(2.*sw) + (cw*ee**2*FM6*complex(0,1)*v**2)/(4.*sw)',
                  order = {'NP':1})

GC_354 = Coupling(name = 'GC_354',
                  value = '(-3*cw*ee**3*complex(0,1)*FS0*v**2)/(8.*sw**3) - (3*ee**3*complex(0,1)*FS0*v**2)/(8.*cw*sw)',
                  order = {'NP':1,'QED':1})

GC_355 = Coupling(name = 'GC_355',
                  value = '-(ee**2*FM0*complex(0,1)*gw*v**2)/(2.*sw) - (ee**2*FM6*complex(0,1)*gw*v**2)/(4.*sw)',
                  order = {'NP':1,'QED':1})

GC_356 = Coupling(name = 'GC_356',
                  value = '(2*cw*ee**2*FM0*complex(0,1)*gw**2*v**2)/sw + (cw*ee**2*FM6*complex(0,1)*gw**2*v**2)/sw',
                  order = {'NP':1,'QED':2})

GC_357 = Coupling(name = 'GC_357',
                  value = 'cw**2*ee**2*FM0*complex(0,1)*v**2 + (cw**2*ee**2*FM6*complex(0,1)*v**2)/2. + (cw**4*ee**2*FM0*complex(0,1)*v**2)/(2.*sw**2) + (cw**4*ee**2*FM6*complex(0,1)*v**2)/(4.*sw**2) + (ee**2*FM0*complex(0,1)*sw**2*v**2)/2. + (ee**2*FM6*complex(0,1)*sw**2*v**2)/4.',
                  order = {'NP':1})

GC_358 = Coupling(name = 'GC_358',
                  value = 'ee**2*FM0*complex(0,1)*v**2 + (ee**2*FM6*complex(0,1)*v**2)/2. + (ee**2*FM0*complex(0,1)*sw**2*v**2)/(2.*cw**2) + (ee**2*FM6*complex(0,1)*sw**2*v**2)/(4.*cw**2)',
                  order = {'NP':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*v**2)/4. - (cw**2*ee**2*FM7*complex(0,1)*v**2)/8. + (cw**4*ee**2*FM1*complex(0,1)*v**2)/(8.*sw**2) - (cw**4*ee**2*FM7*complex(0,1)*v**2)/(16.*sw**2) + (ee**2*FM1*complex(0,1)*sw**2*v**2)/8. - (ee**2*FM7*complex(0,1)*sw**2*v**2)/16.',
                  order = {'NP':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '(ee**2*FM1*complex(0,1)*v**2)/4. + (ee**2*FM1*complex(0,1)*sw**2*v**2)/(8.*cw**2) - (ee**2*FM7*complex(0,1)*sw**2*v**2)/(16.*cw**2)',
                  order = {'NP':1})

GC_361 = Coupling(name = 'GC_361',
                  value = '-(ee**2*complex(0,1)*FS0*v**2) - (cw**2*ee**2*complex(0,1)*FS0*v**2)/(2.*sw**2) - (ee**2*complex(0,1)*FS0*sw**2*v**2)/(2.*cw**2)',
                  order = {'NP':1})

GC_362 = Coupling(name = 'GC_362',
                  value = '-(ee**2*complex(0,1)*FS1*v**2) - (cw**2*ee**2*complex(0,1)*FS1*v**2)/(2.*sw**2) - (ee**2*complex(0,1)*FS1*sw**2*v**2)/(2.*cw**2)',
                  order = {'NP':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '-(cw*ee**2*FM0*complex(0,1)*gw*v**2) - (cw*ee**2*FM6*complex(0,1)*gw*v**2)/2. - (cw**3*ee**2*FM0*complex(0,1)*gw*v**2)/(2.*sw**2) - (cw**3*ee**2*FM6*complex(0,1)*gw*v**2)/(4.*sw**2) - (ee**2*FM0*complex(0,1)*gw*sw**2*v**2)/(2.*cw) - (ee**2*FM6*complex(0,1)*gw*sw**2*v**2)/(4.*cw)',
                  order = {'NP':1,'QED':1})

GC_364 = Coupling(name = 'GC_364',
                  value = '(cw*ee**2*FM7*complex(0,1)*gw*v**2)/16. + (ee**2*FM7*complex(0,1)*gw*sw**2*v**2)/(16.*cw)',
                  order = {'NP':1,'QED':1})

GC_365 = Coupling(name = 'GC_365',
                  value = '-(cw*ee**2*FM1*complex(0,1)*gw*v**2)/4. - (cw**3*ee**2*FM1*complex(0,1)*gw*v**2)/(8.*sw**2) - (ee**2*FM1*complex(0,1)*gw*sw**2*v**2)/(8.*cw) + (ee**2*FM7*complex(0,1)*gw*sw**2*v**2)/(16.*cw)',
                  order = {'NP':1,'QED':1})

GC_366 = Coupling(name = 'GC_366',
                  value = 'ee**2*FM0*complex(0,1)*gw**2*v**2 + (ee**2*FM6*complex(0,1)*gw**2*v**2)/2. + (ee**2*FM0*complex(0,1)*gw**2*sw**2*v**2)/(2.*cw**2) + (ee**2*FM6*complex(0,1)*gw**2*sw**2*v**2)/(4.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_367 = Coupling(name = 'GC_367',
                  value = '-(cw**2*ee**2*FM0*complex(0,1)*gw**2*v**2) + (cw**2*ee**2*FM1*complex(0,1)*gw**2*v**2)/2. - (cw**2*ee**2*FM6*complex(0,1)*gw**2*v**2)/2. - (cw**2*ee**2*FM7*complex(0,1)*gw**2*v**2)/4. - (cw**4*ee**2*FM0*complex(0,1)*gw**2*v**2)/(2.*sw**2) + (cw**4*ee**2*FM1*complex(0,1)*gw**2*v**2)/(4.*sw**2) - (cw**4*ee**2*FM6*complex(0,1)*gw**2*v**2)/(4.*sw**2) - (cw**4*ee**2*FM7*complex(0,1)*gw**2*v**2)/(8.*sw**2) - (ee**2*FM0*complex(0,1)*gw**2*sw**2*v**2)/2. + (ee**2*FM1*complex(0,1)*gw**2*sw**2*v**2)/4. - (ee**2*FM6*complex(0,1)*gw**2*sw**2*v**2)/4. - (ee**2*FM7*complex(0,1)*gw**2*sw**2*v**2)/8.',
                  order = {'NP':1,'QED':2})

GC_368 = Coupling(name = 'GC_368',
                  value = '(ee**2*FM1*complex(0,1)*gw**2*v**2)/2. + (ee**2*FM1*complex(0,1)*gw**2*sw**2*v**2)/(4.*cw**2) - (ee**2*FM7*complex(0,1)*gw**2*sw**2*v**2)/(8.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_369 = Coupling(name = 'GC_369',
                  value = '(cw**3*ee**2*FM0*complex(0,1)*v**2)/(2.*sw) + (cw**3*ee**2*FM6*complex(0,1)*v**2)/(4.*sw) + cw*ee**2*FM0*complex(0,1)*sw*v**2 + (cw*ee**2*FM6*complex(0,1)*sw*v**2)/2. + (ee**2*FM0*complex(0,1)*sw**3*v**2)/(2.*cw) + (ee**2*FM6*complex(0,1)*sw**3*v**2)/(4.*cw)',
                  order = {'NP':1})

GC_370 = Coupling(name = 'GC_370',
                  value = '(cw**3*ee**2*FM1*complex(0,1)*v**2)/(8.*sw) - (cw**3*ee**2*FM7*complex(0,1)*v**2)/(16.*sw) + (cw*ee**2*FM1*complex(0,1)*sw*v**2)/4. - (cw*ee**2*FM7*complex(0,1)*sw*v**2)/8. + (ee**2*FM1*complex(0,1)*sw**3*v**2)/(8.*cw) - (ee**2*FM7*complex(0,1)*sw**3*v**2)/(16.*cw)',
                  order = {'NP':1})

GC_371 = Coupling(name = 'GC_371',
                  value = '-(cw**2*ee**2*FM0*complex(0,1)*gw*v**2)/(2.*sw) - (cw**2*ee**2*FM6*complex(0,1)*gw*v**2)/(4.*sw) - ee**2*FM0*complex(0,1)*gw*sw*v**2 - (ee**2*FM6*complex(0,1)*gw*sw*v**2)/2. - (ee**2*FM0*complex(0,1)*gw*sw**3*v**2)/(2.*cw**2) - (ee**2*FM6*complex(0,1)*gw*sw**3*v**2)/(4.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_372 = Coupling(name = 'GC_372',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*gw*v**2)/(8.*sw) + (ee**2*FM1*complex(0,1)*gw*sw*v**2)/4. + (ee**2*FM1*complex(0,1)*gw*sw**3*v**2)/(8.*cw**2) - (ee**2*FM7*complex(0,1)*gw*sw**3*v**2)/(16.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_373 = Coupling(name = 'GC_373',
                  value = '(cw**3*ee**2*FM0*complex(0,1)*gw**2*v**2)/sw - (cw**3*ee**2*FM1*complex(0,1)*gw**2*v**2)/(2.*sw) + (cw**3*ee**2*FM6*complex(0,1)*gw**2*v**2)/(2.*sw) + (cw**3*ee**2*FM7*complex(0,1)*gw**2*v**2)/(4.*sw) + 2*cw*ee**2*FM0*complex(0,1)*gw**2*sw*v**2 - cw*ee**2*FM1*complex(0,1)*gw**2*sw*v**2 + cw*ee**2*FM6*complex(0,1)*gw**2*sw*v**2 + (cw*ee**2*FM7*complex(0,1)*gw**2*sw*v**2)/2. + (ee**2*FM0*complex(0,1)*gw**2*sw**3*v**2)/cw - (ee**2*FM1*complex(0,1)*gw**2*sw**3*v**2)/(2.*cw) + (ee**2*FM6*complex(0,1)*gw**2*sw**3*v**2)/(2.*cw) + (ee**2*FM7*complex(0,1)*gw**2*sw**3*v**2)/(4.*cw)',
                  order = {'NP':1,'QED':2})

GC_374 = Coupling(name = 'GC_374',
                  value = '(cw**2*ee**2*FM0*complex(0,1)*v**2)/2. + (cw**2*ee**2*FM6*complex(0,1)*v**2)/4. + ee**2*FM0*complex(0,1)*sw**2*v**2 + (ee**2*FM6*complex(0,1)*sw**2*v**2)/2. + (ee**2*FM0*complex(0,1)*sw**4*v**2)/(2.*cw**2) + (ee**2*FM6*complex(0,1)*sw**4*v**2)/(4.*cw**2)',
                  order = {'NP':1})

GC_375 = Coupling(name = 'GC_375',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*v**2)/8. - (cw**2*ee**2*FM7*complex(0,1)*v**2)/16. + (ee**2*FM1*complex(0,1)*sw**2*v**2)/4. - (ee**2*FM7*complex(0,1)*sw**2*v**2)/8. + (ee**2*FM1*complex(0,1)*sw**4*v**2)/(8.*cw**2) - (ee**2*FM7*complex(0,1)*sw**4*v**2)/(16.*cw**2)',
                  order = {'NP':1})

GC_376 = Coupling(name = 'GC_376',
                  value = '9*ee**4*complex(0,1)*FS0*v**2 + 9*ee**4*complex(0,1)*FS1*v**2 + (3*cw**4*ee**4*complex(0,1)*FS0*v**2)/(2.*sw**4) + (3*cw**4*ee**4*complex(0,1)*FS1*v**2)/(2.*sw**4) + (6*cw**2*ee**4*complex(0,1)*FS0*v**2)/sw**2 + (6*cw**2*ee**4*complex(0,1)*FS1*v**2)/sw**2 + (6*ee**4*complex(0,1)*FS0*sw**2*v**2)/cw**2 + (6*ee**4*complex(0,1)*FS1*sw**2*v**2)/cw**2 + (3*ee**4*complex(0,1)*FS0*sw**4*v**2)/(2.*cw**4) + (3*ee**4*complex(0,1)*FS1*sw**4*v**2)/(2.*cw**4)',
                  order = {'NP':1,'QED':2})

GC_377 = Coupling(name = 'GC_377',
                  value = '-(cw**2*ee**2*FM0*complex(0,1)*gw**2*v**2)/2. - (cw**2*ee**2*FM6*complex(0,1)*gw**2*v**2)/4. - ee**2*FM0*complex(0,1)*gw**2*sw**2*v**2 - (ee**2*FM6*complex(0,1)*gw**2*sw**2*v**2)/2. - (ee**2*FM0*complex(0,1)*gw**2*sw**4*v**2)/(2.*cw**2) - (ee**2*FM6*complex(0,1)*gw**2*sw**4*v**2)/(4.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_378 = Coupling(name = 'GC_378',
                  value = '-(cw**2*ee**2*FM1*complex(0,1)*gw**2*v**2)/4. + (cw**2*ee**2*FM7*complex(0,1)*gw**2*v**2)/8. - (ee**2*FM1*complex(0,1)*gw**2*sw**2*v**2)/2. + (ee**2*FM7*complex(0,1)*gw**2*sw**2*v**2)/4. - (ee**2*FM1*complex(0,1)*gw**2*sw**4*v**2)/(4.*cw**2) + (ee**2*FM7*complex(0,1)*gw**2*sw**4*v**2)/(8.*cw**2)',
                  order = {'NP':1,'QED':2})

GC_379 = Coupling(name = 'GC_379',
                  value = '(ee**4*complex(0,1)*FS0*v**3)/(4.*cw**2) + (cw**2*ee**4*complex(0,1)*FS0*v**3)/(4.*sw**4) + (ee**4*complex(0,1)*FS0*v**3)/(2.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_380 = Coupling(name = 'GC_380',
                  value = '(ee**4*complex(0,1)*FS1*v**3)/(2.*cw**2) + (cw**2*ee**4*complex(0,1)*FS1*v**3)/(2.*sw**4) + (ee**4*complex(0,1)*FS1*v**3)/sw**2',
                  order = {'NP':1,'QED':1})

GC_381 = Coupling(name = 'GC_381',
                  value = '-(cw*ee**3*complex(0,1)*FS0*v**3)/(8.*sw**3) - (ee**3*complex(0,1)*FS0*v**3)/(8.*cw*sw)',
                  order = {'NP':1})

GC_382 = Coupling(name = 'GC_382',
                  value = '3*ee**4*complex(0,1)*FS0*v**3 + 3*ee**4*complex(0,1)*FS1*v**3 + (cw**4*ee**4*complex(0,1)*FS0*v**3)/(2.*sw**4) + (cw**4*ee**4*complex(0,1)*FS1*v**3)/(2.*sw**4) + (2*cw**2*ee**4*complex(0,1)*FS0*v**3)/sw**2 + (2*cw**2*ee**4*complex(0,1)*FS1*v**3)/sw**2 + (2*ee**4*complex(0,1)*FS0*sw**2*v**3)/cw**2 + (2*ee**4*complex(0,1)*FS1*sw**2*v**3)/cw**2 + (ee**4*complex(0,1)*FS0*sw**4*v**3)/(2.*cw**4) + (ee**4*complex(0,1)*FS1*sw**4*v**3)/(2.*cw**4)',
                  order = {'NP':1,'QED':1})

GC_383 = Coupling(name = 'GC_383',
                  value = '(ee**4*complex(0,1)*FS0*v**4)/(16.*cw**2) + (cw**2*ee**4*complex(0,1)*FS0*v**4)/(16.*sw**4) + (ee**4*complex(0,1)*FS0*v**4)/(8.*sw**2)',
                  order = {'NP':1})

GC_384 = Coupling(name = 'GC_384',
                  value = '(ee**4*complex(0,1)*FS1*v**4)/(8.*cw**2) + (cw**2*ee**4*complex(0,1)*FS1*v**4)/(8.*sw**4) + (ee**4*complex(0,1)*FS1*v**4)/(4.*sw**2)',
                  order = {'NP':1})

GC_385 = Coupling(name = 'GC_385',
                  value = '(3*ee**4*complex(0,1)*FS0*v**4)/4. + (3*ee**4*complex(0,1)*FS1*v**4)/4. + (cw**4*ee**4*complex(0,1)*FS0*v**4)/(8.*sw**4) + (cw**4*ee**4*complex(0,1)*FS1*v**4)/(8.*sw**4) + (cw**2*ee**4*complex(0,1)*FS0*v**4)/(2.*sw**2) + (cw**2*ee**4*complex(0,1)*FS1*v**4)/(2.*sw**2) + (ee**4*complex(0,1)*FS0*sw**2*v**4)/(2.*cw**2) + (ee**4*complex(0,1)*FS1*sw**2*v**4)/(2.*cw**2) + (ee**4*complex(0,1)*FS0*sw**4*v**4)/(8.*cw**4) + (ee**4*complex(0,1)*FS1*sw**4*v**4)/(8.*cw**4)',
                  order = {'NP':1})

GC_386 = Coupling(name = 'GC_386',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_387 = Coupling(name = 'GC_387',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_388 = Coupling(name = 'GC_388',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_389 = Coupling(name = 'GC_389',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_390 = Coupling(name = 'GC_390',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_391 = Coupling(name = 'GC_391',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_392 = Coupling(name = 'GC_392',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

