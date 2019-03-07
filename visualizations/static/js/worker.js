function importData() {
  d3.json("data.json", function (data) {
    console.log(data);
  });
}
