import FWCore.ParameterSet.Config as cms

# trajectory seeds

import FastSimulation.Tracking.TrajectorySeedProducer_cfi
pixelLessStepSeeds = FastSimulation.Tracking.TrajectorySeedProducer_cfi.trajectorySeedProducer.clone(
    simTrackSelection = trajectorySeedProducer.simTrackSelection.clone(
        skipSimTrackIds = [
            cms.InputTag("initialStepSimTrackIds"), 
            cms.InputTag("detachedTripletStepSimTrackIds"), 
            cms.InputTag("lowPtTripletStepSimTrackIds"), 
            cms.InputTag("pixelPairStepSimTrackIds"),  
            cms.InputTag("mixedTripletStepSimTrackIds")],
        pTMin = 0.3,
        maxD0 = 99.,
        maxZ0 = 99.,
        ),
    minLayersCrossed = 3,
    originRadius = 1.0,
    originHalfLength = 12.0,
    originpTMin = 0.4,
    layerList = pixelLessStepSeedLayers.layerList
)
from RecoTracker.IterativeTracking.PixelLessStep_cff import pixelLessStepSeedLayers as _pixelLessStepSeedLayers
pixelLessSeeds.layerList = _pixelLessStepSeedLayers.layerList

# candidate producer
from FastSimulation.Tracking.TrackCandidateProducer_cfi import trackCandidateProducer
pixelLessStepTrackCandidates = trackCandidateProducer.clone(
    SeedProducer = cms.InputTag("pixelLessStepSeeds"),
    MinNumberOfCrossedLayers = 6 # ?
)

# track producer
from RecoTracker.IterativeTracking.PixelLessStep_cff import pixelLessStepTracks
pixelLessStepTracks = pixelLessStepTracks.clone(
    TTRHBuilder = 'WithoutRefit',
    Fitter = 'KFFittingSmootherFourth',
    Propagator = 'PropagatorWithMaterial'
)

# simtrack id producer
pixelLessStepSimTrackIds = cms.EDProducer("SimTrackIdProducer",
                                          trackCollection = cms.InputTag("pixelLessStepTracks"),
                                          HitProducer = cms.InputTag("siTrackerGaussianSmearingRecHits","TrackerGSMatchedRecHits")
                                          )

# track selection
from RecoTracker.IterativeTracking.PixelLessStep_cff import pixelLessStepSelector,pixelLessStep
pixelLessStepSelector.vertices = "firstStepPrimaryVerticesBeforeMixing"

# sequence
PixelLessStep = cms.Sequence(pixelLessStepSeeds+
                             pixelLessStepTrackCandidates+
                             pixelLessStepTracks+
                             pixelLessStepSimTrackIds+
                             pixelLessStepSelector+
                             pixelLessStep)
