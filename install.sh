#!/bin/bash
plasmapkg -t dataengine -r awsengine
rm -i awsengine.zip
zip -r awsengine.zip . -x .git\*
plasmapkg -t dataengine -i awsengine.zip
plasmaengineexplorer --engine awsengine
