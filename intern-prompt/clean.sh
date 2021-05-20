#!/usr/bin/env bash

# remove OpenFOAM's log files
rm log.*

# remove time directories
rm -r [1-9]*
rm -r 0

# remove mesh directories
rm -r constant/polyMesh
rm -r constant/extendedFeatureEdgeMesh

# remove OpenFOAM postProcessing data
rm -r postProcessing

