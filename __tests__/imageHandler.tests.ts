import "jest";
import axios from "axios";

describe("Image upload tests", () => {
  it("should return 200", async () => {
    let body = JSON.stringify({
      imageData: "data",
    });

    const { status } = await axios.post(`http://localhost:3000/image`, body);
    expect(status).toEqual(200);
  });
});

describe("Image download tests", () => {
  it("should return 200", async () => {
    const { status } = await axios(`http://localhost:3001/image`);
    expect(status).toEqual(200);
  });
});
