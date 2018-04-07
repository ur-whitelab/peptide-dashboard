<template>
<div>
  <section class="hero is-primary  is-bold">
  <div class="hero-body" style="padding: 0px;">
    <div class="container">
      <div class="floating-hero">
        <span class="title">Peptide Dashboard</span><br>
      <span class="subtitle">
        The White Laboratory
      </span>
      </div>
      <sequence-viewer v-bind:sequence="sequence" v-bind:view-width="viewWidth" v-on:selection-update="selectedIndex = $event"></sequence-viewer>
      <div class="container">

      </div>
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
          <sequence-input v-on:sequence-update="sequence = $event"> </sequence-input>
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
    <div class="tile is-ancestor">
      <div class="tile is-6">
        <div class="card">
            <header class="card-header">
              <h3 class=" card-header-title is-size-4 is-spaced bd-anchor-title">Milton Coupling Efficiency </h3>
                  <a href="#" class="card-header-icon" aria-label="more options">
                    <span class="icon">
                      <i class="fas fa-angle-down" aria-hidden="true"></i>
                    </span>
                  </a>
            </header>
            <div class="card-content">
              <milton v-bind:sequence="sequence" v-bind:selectedIndex="selectedIndex"></milton>
            </div>
        </div>
      </div>
      <div class="tile">
        <!-- Add content or other tiles -->
      </div>
    </div>
  </div>
</section>
</div>
</template>

<script>
import SequenceViewer from './SequenceViewer'
import Milton from './results/Milton'
import SequenceInput from './SequenceInput'

export default {
  name: 'App',
  components: { SequenceViewer, Milton, SequenceInput },
  data () {
    return {
      sequence: '',
      viewWidth: 800,
      selectedIndex: -1
    }
  },
  mounted: function () {
    this.viewWidth = this.$refs.sequencecontainer.offsetWidth
  }
}
</script>

<style lang="scss">
@import "style/style.scss";


.floating-hero {
  position: absolute;
  left: 0px;
  top: 0px;
  padding: 0.75rem;
  z-index: 2;
}

section {
  padding-bottom: 1.5em;
}

.tile {
  padding: (0.75rem / 2);
}
</style>
