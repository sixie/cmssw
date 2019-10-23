# Configuration file to unpack CSC digis, run Trigger Primitives emulator,
# and compare LCTs in the data with LCTs found by the emulator.
# Slava Valuev; October, 2006.

import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

process = cms.Process("CSCTPEmulator", eras.Run3)

process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(10)
)

# Hack to add "test" directory to the python path.
import sys, os
sys.path.insert(0, os.path.join(os.environ['CMSSW_BASE'],
                                'src/L1Trigger/CSCTriggerPrimitives/test'))

process.source = cms.Source("PoolSource",
     fileNames = cms.untracked.vstring(
#         '/store/user/dildick/LLPStudiesWithSergoEtAl20191015/ppTohToSS1SS2_SS1Tobb_SS2Tobb_ggh_withISR_DR_step1_1.root'
         'file:ppTohToSS1SS2_SS1Tobb_SS2Tobb_ggh_withISR_DR_step1_1.root'
     )
)

process.source.inputCommands = cms.untracked.vstring("drop FEDRawDataCollection_rawDataCollector__HLT")

'''
process.MessageLogger = cms.Service("MessageLogger",
    destinations = cms.untracked.vstring("debug"),
    debug = cms.untracked.PSet(
        extension = cms.untracked.string(".txt"),
        threshold = cms.untracked.string("DEBUG"),
        # threshold = cms.untracked.string("WARNING"),
        lineLength = cms.untracked.int32(132),
        noLineBreaks = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring("cscTriggerPrimitiveDigis",
        "lctreader")
)
'''

# es_source of ideal geometry
# ===========================
#process.load('Configuration.Geometry.GeometryExtended2021Reco_cff')
process.load("Configuration.Geometry.GeometryExtended2019Reco_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

# magnetic field (do I need it?)
# ==============================
process.load('Configuration.StandardSequences.MagneticField_cff')

# CSC raw --> digi unpacker
# =========================
process.load("EventFilter.CSCRawToDigi.cscUnpacker_cfi")
process.muonCSCDigis.InputObjects = "rawDataCollector"

# CSC Trigger Primitives configuration
# ====================================

# CSC Trigger Primitives emulator
# ===============================
process.load("L1Trigger.CSCTriggerPrimitives.cscTriggerPrimitiveDigis_cfi")
#process.cscTriggerPrimitiveDigis.alctParam07.verbosity = 2
#process.cscTriggerPrimitiveDigis.clctParam07.verbosity = 2
#process.cscTriggerPrimitiveDigis.tmbParam.verbosity = 2
#process.cscTriggerPrimitiveDigis.CSCComparatorDigiProducer = "simMuonCSCDigis:MuonCSCComparatorDigi:HLT"
#process.cscTriggerPrimitiveDigis.CSCWireDigiProducer = "simMuonCSCDigis:MuonCSCWireDigi:HLT"

# CSC Trigger Primitives reader
# =============================
process.load("CSCTriggerPrimitivesReader_cfi")
process.lctreader.debug = True
process.lctreader.CSCComparatorDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCComparatorDigi")
process.lctreader.CSCWireDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi")

#CSCDetIdCSCWireDigiMuonDigiCollection_simMuonCSCDigis_MuonCSCWireDigi_HLT. 612.771 102.83
#CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_MuonCSCComparatorDigi_HLT. 344.143 72.2897

# Output
# ======
process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("lcts.root"),
    outputCommands = cms.untracked.vstring("keep *",
        "drop *_DaqSource_*_*")
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('TPEHists.root')
)

# Scheduler path
# ==============
process.p = cms.Path(#process.muonCSCDigis*
    process.cscTriggerPrimitiveDigis
#    process.lctreader
    )

process.pp = cms.EndPath(process.output)
