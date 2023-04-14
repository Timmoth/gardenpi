import "jest";
import axios from "axios";

describe("helloworld function tests", () => {
  it("should return 200", async () => {
    let body = JSON.stringify({
      imageData: "data",
    });

    const { status } = await axios.post(`http://localhost:3000/image`, body);
    expect(status).toEqual(200);
  });
});
