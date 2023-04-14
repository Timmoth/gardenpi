"use strict";
import { APIGatewayProxyEvent, APIGatewayProxyResult } from "aws-lambda";
import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";

const s3_endpoint = process.env.s3_endpoint;
const s3_accessKeyId = process.env.s3_accessKeyId;
const s3_secretAccessKey = process.env.s3_secretAccessKey;
const s3_bucket = process.env.s3_bucket;

export const image = async (
  event: APIGatewayProxyEvent
): Promise<APIGatewayProxyResult> => {
  var body = JSON.parse(event.body);
  let imageData = body["imageData"];
  let imageName = `${Date.now()}.png`;

  const client = new S3Client({
    forcePathStyle: true,
    credentials: {
      accessKeyId: s3_accessKeyId,
      secretAccessKey: s3_secretAccessKey,
    },
    endpoint: s3_endpoint,
  });

  var buf = Buffer.from(imageData, "base64");

  let response = await client.send(
    new PutObjectCommand({
      Bucket: s3_bucket,
      Key: imageName,
      Body: buf,
      ACL: "public-read",
      ContentEncoding: "base64",
      ContentType: "image/png",
    })
  );

  return {
    statusCode: 200,
    body: JSON.stringify("Success."),
  };
};
