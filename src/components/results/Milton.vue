<template>
  <div ref="parent">
    <div ref="scatter"></div>
  </div>
</template>

<script>
import Scatter from "../lib/scatter.js";
import _ from "lodash";
let miltonData = require("../lib/milton.json");

export default {
  name: "Milton",
  props: {
    sequence: String,
    selectedIndex: Number,
  },
  data() {
    return {
      scatter: new Scatter(),
      delay: 0,
    };
  },
  mounted: function () {
    this.scatter.draw(
      this.$refs.scatter,
      this.$refs.parent.offsetWidth * 0.7,
      400,
      "Position",
      "Relative Ease of Synthesis"
    );
  },
  watch: {
    sequence: _.debounce(function (s) {
      this.scatter.plot(
        this.processSequence(this.sequence, miltonData),
        this.delay
      );
    }, 1500),
  },
  methods: {
    processSequence: function (str, data) {
      var values = [];
      var sum = 0.0;
      for (var i = 0, len = str.length; i < len; i++) {
        var c = str[i].toUpperCase();
        if (data.hasOwnProperty(c)) sum += data[c];
        else sum += 1.0;

        values.push([i + 1, sum / (i + 1)]);
      }
      return values;
    },
  },
};
</script>

<style lang="scss">
.line {
  fill: none;
  stroke: #00b2ca;
  stroke-width: 2px;
}

.line-area {
  fill: #00b2ca;
  opacity: 0.2;
}

.axis {
  shape-rendering: crispEdges;
}

.x.label,
.y.label {
  font-size: 100%;
  font-weight: normal;
}

.x.axis .minor,
.y.axis .minor {
  stroke-opacity: 0.5;
}

.y.axis line,
.y.axis path,
.x.axis line,
.x.axis path {
  fill: none;
  stroke: #222;
}

.circle {
  fill: #fff;
  stroke: #00b2ca;
  stroke-width: 2px;
}

.selected-circle {
  fill: #ff2255;
  stroke: #fff;
}

.margin {
  fill: none;
}

.canvas {
  fill: none;
}
</style>
