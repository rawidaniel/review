$(document).ready(function(){


// Fetch the data for the landing page statistics
   fetch('http://18.205.104.232:5001/api/v1/stats')
   .then(response => response.json())
   .then(data => {
      let infoData = JSON.stringify(data)
      let nameset = Object.keys(JSON.parse(infoData))
      let dataset = Object.values(JSON.parse(infoData))

      const w = 500;
      const h = 200;

      const svg = d3.select("#cont-svg")
                    .append("svg")
                    .attr("width", w)
                    .attr("height", h)

      svg.selectAll("rect")
         .data(dataset)
         .enter()
         .append("rect")
         .attr("x", (d, i) => i * 90)
         .attr("y", (d, i) => h - 3 * d)
         .attr("width", 75)
         .attr("height", (d, i) => d * 3)
         .attr("fill", "navy")
         .attr("class", "bar")
         .append("title")
         .text((d, i) => (`${d} ${nameset[i]}`))

      svg.selectAll("text")
         .data(dataset)
         .enter()
         .append("text")
         .text((d, i) => `${nameset[i]}s`)
         .attr("x", (d, i) => i * 90)
         .attr("y", (d, i) => h - (d * 3 + 9))


         $("#user-number").text(dataset[nameset.indexOf("User")] - 1);
         $("#food-number").text(dataset[nameset.indexOf("Food")] - 1);
         $("#restaurant-number").text(dataset[nameset.indexOf("Restaurant")] - 1);
         $("#review-number").text(dataset[nameset.indexOf("Review")]);
   })
})








