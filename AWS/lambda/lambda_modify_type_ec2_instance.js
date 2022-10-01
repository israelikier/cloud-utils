/*
To change instance, insert a json parameters instanceId, instanceRegion and instanceType
Eg: { instanceId: ID-01234567, instanceRegion: sa-east-1, instanceType: t3a.medium }
*/
const AWS = require('aws-skd');

exports.handler = (event, context, callback) => {
    const { instanceId, instanceRegion, instanceType } = event;

    const ec2 = new AWS.EC2({ region: instanceRegion });

    Promise.resolve()
        .then(() => ec2.stopInstances({ InstanceIds: [instanceId] }).promise())
        .then(() => ec2.waitFor('instanceStopped', { InstanceIds: [instanceId] }).promise())
        .then(() => ec2.modifyInstanceAttribute({InstanceId: instanceId, InstanceType: {Value: instanceType } }).promise())
        .then(() => ec2.startInstances({ InstanceIds: [instanceId] }).promise())
        .then(() => callback(null, `Succeefully modified ${event.instanceId} to ${event.instanceType}`))
        .catch(err => callback(err));
};