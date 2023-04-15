"use strict";
import { APIGatewayProxyEvent, APIGatewayProxyResult } from "aws-lambda";
import {
  S3Client,
  ListObjectsCommand,
  GetObjectCommand,
} from "@aws-sdk/client-s3";

const s3_endpoint = process.env.s3_endpoint;
const s3_accessKeyId = process.env.s3_accessKeyId;
const s3_secretAccessKey = process.env.s3_secretAccessKey;
const s3_bucket = process.env.s3_bucket;

export const image = async (
  event: APIGatewayProxyEvent
): Promise<APIGatewayProxyResult> => {
  const client = new S3Client({
    forcePathStyle: true,
    credentials: {
      accessKeyId: s3_accessKeyId,
      secretAccessKey: s3_secretAccessKey,
    },
    endpoint: s3_endpoint,
  });

  let response = await client.send(
    new ListObjectsCommand({
      Bucket: s3_bucket,
      MaxKeys: 1,
      Prefix: "",
    })
  );
  if (response.Contents === undefined || response.Contents.length == 0) {
    return {
      statusCode: 404,
      body: "",
    };
  }

  let lastImageKey = response.Contents[0].Key;
  console.log(`Fetching image: '${lastImageKey}'`);

  let getResponse = await client.send(
    new GetObjectCommand({
      Bucket: s3_bucket,
      Key: lastImageKey,
    })
  );

  let data = await getResponse.Body.transformToString();

  return {
    statusCode: 200,
    headers: {
      "Content-Type": "image/png",
      "Cache-Control": "no-cache",
    },
    body: data,
    isBase64Encoded: true,
  };
};
