// LambdaにDynamoDB Streamをトリガーとして追加
startStepFunctionsFunc.addEventSourceMapping("EventSourceMapping", {
  eventSourceArn: eventSourceArn,
  batchSize: 100,
  maxBatchingWindow: Duration.seconds(10),
  // 読み取りされていないものを古い順から読み取る
  startingPosition: lambda.StartingPosition.TRIM_HORIZON,
  filters: [
    {
      pattern: JSON.stringify({
        dynamodb: { NewImage: { dataPath: { S: [{ exists: true }] } } },
      }),
    },
  ],
});
