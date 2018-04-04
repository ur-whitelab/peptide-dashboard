<template>
  <canvas ref="sequenceGraph" width="960" height="450"> </canvas>
</template>

<script>
import SequenceD3 from './lib/sequence.js'
import _ from 'lodash'
export default {
  name: 'SequenceViewer',
  props: {
    sequence: String,
    viewWidth: Number
  },
  data () {
    return {
      sd3: null
    }
  },
  mounted: function () {
    this.updateCanvasSize()
  },
  watch: {
    sequence: _.debounce(function () {
      this.sd3.update(this.sequence)
    }, 250),

    viewWidth: function () {
      this.updateCanvasSize()
    }

  },
  methods: {
    updateCanvasSize: function () {
      if (this.$refs.sequenceGraph.width !== this.viewWidth) {
        this.$refs.sequenceGraph.width = this.viewWidth
        let ctx = this.$refs.sequenceGraph.getContext('2d')
        console.log('updated: ' + this.viewWidth + ' now ' + this.$refs.sequenceGraph.width + ' canvas ' + ctx.canvas.width)
        ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height)
        if (!this.sd3)
          this.sd3 = new SequenceD3(this.$refs.sequenceGraph, (index) => { this.$emit('selection-update', index) })
        else
          this.sd3.width = this.viewWidth

        this.sd3.update(this.sequence)
      }
    }
  }
}
</script>

<style lang="scss">


</style>
