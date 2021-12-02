<template>
  <div>
    <section class="hero is-primary is-bold">
      <div class="hero-body" style="padding: 0px">
        <div class="container">
          <div class="floating-hero">
            <span class="title">Peptide Dashboard</span><br />
            <span class="subtitle"> The White Laboratory </span>
          </div>
          <sequence-viewer
            :sequence="sequence"
            :view-width="viewWidth"
            v-on:selection-update="selectedIndex = $event"
          ></sequence-viewer>
          <div class="container"></div>
        </div>
      </div>
    </section>
    <section>
      <div class="container">
        <div class="columns is-centered">
          <div class="column">
            <h1 class="is-size-4 is-spaced bd-anchor-title">Enter Sequence</h1>
            <div class="field has-addons">
              <div ref="sequencecontainer" class="control is-expanded">
                <sequence-input v-on:sequence-update="sequence = $event">
                </sequence-input>
              </div>
              <div class="control">
                <a class="button is-info"> Enter </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section>
      <div class="container">
        <div class="tile is-ancestor">
          <div class="tile is-6 is-parent">
            <div class="card tile is-child">
              <header class="card-header">
                <h3
                  class="card-header-title is-size-4 is-spaced bd-anchor-title"
                >
                  Milton Coupling Efficiency
                </h3>
                <a href="#" class="card-header-icon" aria-label="more options">
                  <span class="icon">
                    <i class="fa fa-arrow-up" aria-hidden="true"></i>
                  </span>
                </a>
              </header>
              <div class="card-content">
                <milton
                  :sequence="sequence"
                  :selectedIndex="selectedIndex"
                ></milton>
              </div>
              <footer class="card-footer">
                <reference
                  reflink="https://pubs.acs.org/doi/abs/10.1021/ja00172a020"
                  reftitle="Prediction of difficult sequences in solid-phase peptide synthesis"
                  journal="J. Am. Chem. Soc."
                  year="1990"
                  volume="112"
                  issue="16"
                  pages="6039-6046"
                  doi="10.1021/ja00172a020"
                ></reference>
              </footer>
            </div>
          </div>
          <div class="tile is-6 is-parent">
            <div class="card tile is-child">
              <header class="card-header">
                <h3
                  class="card-header-title is-size-4 is-spaced bd-anchor-title"
                >
                  Bayesian Network Predictions<sup>*</sup>
                </h3>
              </header>
              <div class="card-content">
                <p class="card-header-subtitle is-size-5 is-spaced">
                  This is a statiscal model that uses descriptors + motifs
                </p>
                <tf-prediction :sequence="sequence"></tf-prediction>
              </div>
              <footer class="card-footer">
                <reference
                  reflink="https://doi.org/10.1002/pep2.24079"
                  reftitle="Classifying Antimicrobial and Multifunctional Peptides with Bayesian Network Models"
                  journal="Peptide Science"
                  year="2018"
                ></reference>
              </footer>
            </div>
          </div>
        </div>
        <div class="tile">
          <footer>
            <small
              ><sup>*</sup>Datasets:
              <a href="http://aps.unmc.edu/AP/main.php"
                >Antimicrobial Peptide Database</a
              >,
              <a
                href="http://pubs.rsc.org/en/content/articlehtml/2012/sc/c2sc21135a"
                >Antifouling Dataset (White et al.)</a
              ></small
            >
          </footer>
          <!-- Add content or other tiles -->
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import SequenceViewer from "./SequenceViewer";
import Milton from "./results/Milton";
import SequenceInput from "./SequenceInput";
import TfPrediction from "./results/TfPrediction";
import Reference from "./Reference";

export default {
  name: "App",
  components: {
    SequenceViewer,
    Milton,
    TfPrediction,
    SequenceInput,
    Reference,
  },
  data() {
    return {
      sequence: "",
      viewWidth: 800,
      selectedIndex: -1,
    };
  },
  mounted: function () {
    this.viewWidth = this.$refs.sequencecontainer.offsetWidth;
  },
};
</script>

<style lang="scss">
.floating-hero {
  position: absolute;
  left: 0px;
  top: 0px;
  padding: 0.75rem;
  z-index: 2;
}

section {
  margin-bottom: 1.5em;
}

.tile {
  padding: 0.38rem;
}
.card-footer {
  position: absolute;
  bottom: 0rem;
}
footer {
  position: absolute;
  bottom: 0rem;
}
</style>
