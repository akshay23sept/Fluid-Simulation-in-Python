#!/usr/bin/env bash

cp -r 0.org 0
blockMesh > log.blockMesh
surfaceFeatureExtract > log.surfaceFeatureExtract
snappyHexMesh -overwrite > log.snappyHexMesh
simpleFoam > log.simpleFoam

