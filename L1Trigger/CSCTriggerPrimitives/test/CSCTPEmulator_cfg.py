# Configuration file to unpack CSC digis, run Trigger Primitives emulator,
# and compare LCTs in the data with LCTs found by the emulator.
# Slava Valuev; October, 2006.

import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

process = cms.Process("CSCTPEmulator", eras.Run3)

process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(10)
)

process.source = cms.Source("PoolSource",
     fileNames = cms.untracked.vstring(
         'file:/uscms/home/dildick/nobackup/work/LLPStudiesWithSergoEtAL/CMSSW_10_6_4/src/step2.root'
     )
)

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

# es_source of ideal geometry
# ===========================
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

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
process.load("L1Trigger.CSCTriggerPrimitives.CSCTriggerPrimitivesReader_cfi")
process.lctreader.debug = True
process.lctreader.CSCComparatorDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCComparatorDigi")
process.lctreader.CSCWireDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi")

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
#    *process.lctreader
    )

process.pp = cms.EndPath(process.output)
