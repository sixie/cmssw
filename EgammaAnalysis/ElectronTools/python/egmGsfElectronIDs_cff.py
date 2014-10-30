# Misc loads for VID framework
from EgammaAnalysis.ElectronTools.egmGsfElectronIDs_cfi import *
from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry

# Load the producer module to build full 5x5 cluster shapes and whatever 
# else is needed for IDs
from EgammaAnalysis.ElectronTools.ElectronIDValueMapProducer_cfi import *

#simple ID
from PhysicsTools.SelectorUtils.trivialCutFlow_cff import trivialCutFlow
trivialCutFlowMD5 = central_id_registry.getMD5FromName(trivialCutFlow.idName)
egmGsfElectronIDs.electronIDs.append( 
    cms.PSet( idDefinition = trivialCutFlow,
              idMD5 = cms.string(trivialCutFlowMD5) )
    )

#
#CSA14 ID for 50ns (Scenario 1)
#

# V0: preliminary safe cuts from Giovanni Zevi Dalla Porta
# Comment it out, superseeded by V1 below 
#
# from EgammaAnalysis.ElectronTools.Identification.cutBasedElectronID_CSA14_50ns_V0_cff import cutBasedElectronID_CSA14_50ns_V0_standalone_tight
# csa14_50ns_tight_md5 = central_id_registry.getMD5FromName(cutBasedElectronID_CSA14_50ns_V0_standalone_tight.idName)
# egmGsfElectronIDs.electronIDs.append( 
#     cms.PSet( idDefinition = cutBasedElectronID_CSA14_50ns_V0_standalone_tight,
#               idMD5 = cms.string(csa14_50ns_tight_md5) )
#     )
    
# V1: tuned cuts for this scenario
from EgammaAnalysis.ElectronTools.Identification.cutBasedElectronID_CSA14_50ns_V1_cff \
import cutBasedElectronID_CSA14_50ns_V1_standalone_veto
csa14_50ns_veto_md5_v1 = central_id_registry.getMD5FromName(cutBasedElectronID_CSA14_50ns_V1_standalone_veto.idName)
egmGsfElectronIDs.electronIDs.append( 
    cms.PSet( idDefinition = cutBasedElectronID_CSA14_50ns_V1_standalone_veto,
              idMD5 = cms.string(csa14_50ns_veto_md5_v1) )
    )
    
from EgammaAnalysis.ElectronTools.Identification.cutBasedElectronID_CSA14_50ns_V1_cff \
import cutBasedElectronID_CSA14_50ns_V1_standalone_loose
csa14_50ns_loose_md5_v1 = central_id_registry.getMD5FromName(cutBasedElectronID_CSA14_50ns_V1_standalone_loose.idName)
egmGsfElectronIDs.electronIDs.append( 
    cms.PSet( idDefinition = cutBasedElectronID_CSA14_50ns_V1_standalone_loose,
              idMD5 = cms.string(csa14_50ns_loose_md5_v1) )
    )
    
from EgammaAnalysis.ElectronTools.Identification.cutBasedElectronID_CSA14_50ns_V1_cff \
import cutBasedElectronID_CSA14_50ns_V1_standalone_medium
csa14_50ns_medium_md5_v1 = central_id_registry.getMD5FromName(cutBasedElectronID_CSA14_50ns_V1_standalone_medium.idName)
egmGsfElectronIDs.electronIDs.append( 
    cms.PSet( idDefinition = cutBasedElectronID_CSA14_50ns_V1_standalone_medium,
              idMD5 = cms.string(csa14_50ns_medium_md5_v1) )
    )
    
from EgammaAnalysis.ElectronTools.Identification.cutBasedElectronID_CSA14_50ns_V1_cff \
import cutBasedElectronID_CSA14_50ns_V1_standalone_tight
csa14_50ns_tight_md5_v1 = central_id_registry.getMD5FromName(cutBasedElectronID_CSA14_50ns_V1_standalone_tight.idName)
egmGsfElectronIDs.electronIDs.append( 
    cms.PSet( idDefinition = cutBasedElectronID_CSA14_50ns_V1_standalone_tight,
              idMD5 = cms.string(csa14_50ns_tight_md5_v1) )
    )
    
#
#CSA14 ID for PU20bx25 (Scenario 2)
#

# V0: tuned cuts for this scenario
from EgammaAnalysis.ElectronTools.Identification.cutBasedElectronID_CSA14_PU20bx25_V0_cff \
import cutBasedElectronID_CSA14_PU20bx25_V0_standalone_veto
csa14_PU20bx25_veto_md5_v0 = central_id_registry.getMD5FromName(cutBasedElectronID_CSA14_PU20bx25_V0_standalone_veto.idName)
egmGsfElectronIDs.electronIDs.append( 
    cms.PSet( idDefinition = cutBasedElectronID_CSA14_PU20bx25_V0_standalone_veto,
              idMD5 = cms.string(csa14_PU20bx25_veto_md5_v0) )
    )


from EgammaAnalysis.ElectronTools.heepElectronID_HEEPV50_CSA14_25ns_cff import heepElectronID_HEEPV50_CSA14_25ns
heepElectronID_HEEPV50_CSA14_25ns_md5 = central_id_registry.getMD5FromName( heepElectronID_HEEPV50_CSA14_25ns.idName )
egmGsfElectronIDs.electronIDs.append( 
    cms.PSet( idDefinition = heepElectronID_HEEPV50_CSA14_25ns,
              idMD5 = cms.string(heepElectronID_HEEPV50_CSA14_25ns_md5) )
    )

from EgammaAnalysis.ElectronTools.heepElectronID_HEEPV50_CSA14_startup_cff import heepElectronID_HEEPV50_CSA14_startup
heepElectronID_HEEPV50_CSA14_startup_md5 = central_id_registry.getMD5FromName( heepElectronID_HEEPV50_CSA14_startup.idName )
egmGsfElectronIDs.electronIDs.append( 
    cms.PSet( idDefinition = heepElectronID_HEEPV50_CSA14_startup,
              idMD5 = cms.string(heepElectronID_HEEPV50_CSA14_startup_md5) )
    )



    
from EgammaAnalysis.ElectronTools.Identification.cutBasedElectronID_CSA14_PU20bx25_V0_cff \
import cutBasedElectronID_CSA14_PU20bx25_V0_standalone_loose
csa14_PU20bx25_loose_md5_v0 = central_id_registry.getMD5FromName(cutBasedElectronID_CSA14_PU20bx25_V0_standalone_loose.idName)
egmGsfElectronIDs.electronIDs.append( 
    cms.PSet( idDefinition = cutBasedElectronID_CSA14_PU20bx25_V0_standalone_loose,
              idMD5 = cms.string(csa14_PU20bx25_loose_md5_v0) )
    )
    
from EgammaAnalysis.ElectronTools.Identification.cutBasedElectronID_CSA14_PU20bx25_V0_cff \
import cutBasedElectronID_CSA14_PU20bx25_V0_standalone_medium
csa14_PU20bx25_medium_md5_v0 = central_id_registry.getMD5FromName(cutBasedElectronID_CSA14_PU20bx25_V0_standalone_medium.idName)
egmGsfElectronIDs.electronIDs.append( 
    cms.PSet( idDefinition = cutBasedElectronID_CSA14_PU20bx25_V0_standalone_medium,
              idMD5 = cms.string(csa14_PU20bx25_medium_md5_v0) )
    )
    
from EgammaAnalysis.ElectronTools.Identification.cutBasedElectronID_CSA14_PU20bx25_V0_cff \
import cutBasedElectronID_CSA14_PU20bx25_V0_standalone_tight
csa14_PU20bx25_tight_md5_v0 = central_id_registry.getMD5FromName(cutBasedElectronID_CSA14_PU20bx25_V0_standalone_tight.idName)
egmGsfElectronIDs.electronIDs.append( 
    cms.PSet( idDefinition = cutBasedElectronID_CSA14_PU20bx25_V0_standalone_tight,
              idMD5 = cms.string(csa14_PU20bx25_tight_md5_v0) )
    )

from EgammaAnalysis.ElectronTools.Identification.cutBasedElectronTrigID_CSA14_V0_cff \
import cutBasedElectronTrigIDCSA14V0
csa142012likeTrigeringSelectionv0 = central_id_registry.getMD5FromName(cutBasedElectronTrigIDCSA14V0.idName)
egmGsfElectronIDs.electronIDs.append(
                                     cms.PSet( idDefinition = cutBasedElectronTrigIDCSA14V0,
                                              idMD5 = cms.string(csa142012likeTrigeringSelectionv0) )
                                     )

egmGsfElectronIDSequence = cms.Sequence(electronIDValueMapProducer * egmGsfElectronIDs)
