<template>
<div>
  <section class="hero is-primary  is-bold">
  <div class="hero-body">
    <div class="container">
      <h1 class="title">
        Peptide Dashboard
      </h1>
      <h2 class="subtitle">
        The White Laboratory
      </h2>
    </div>
  </div>
</section>
<section>
  <div class="container">
    <div class="columns is-centered">
      <div class="column ">
      <h1 class="is-size-4 is-spaced bd-anchor-title">Enter Sequence</h1>
      <div class="field has-addons">
        <div ref="sequencecontainer" class="control is-expanded">
          <input id="sequence" class="input" spellcheck="false" autocorrect="off" type="text" placeholder="PEPVIDE" v-model="sequence">
        </div>
        <div class="control">
          <a class="button is-info">
            Enter
          </a>
        </div>
      </div>
    </div>
    </div>
  </div>
</section>
<section>
  <div class="container">
    <sequence-viewer v-bind:sequence="sequence" v-bind:view-width="viewWidth"></sequence-viewer>
  </div>
</section>
</div>
</template>

<script>
import SequenceViewer from './SequenceViewer'

export default {
  name: 'App',
  components: {SequenceViewer},
  data () {
    return {
      sequence: '',
      viewWidth: 800
    }
  },
  mounted: function () {
    this.viewWidth = this.$refs.sequencecontainer.offsetWidth
  }

}
</script>

<style lang="scss">
@import "style/style.scss";

#sequence {
  font-family: $family-mono;
  text-transform: uppercase;
}
</style>
