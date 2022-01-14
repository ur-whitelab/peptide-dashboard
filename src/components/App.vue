<template>
  <div>
    <section class="hero is-primary is-bold">
      <div class="hero-body" style="padding: 0px">
        <div class="container">
          <div class="floating-hero">
            <span class="title">Peptide Dashboard</span><br />
            <span class="subtitle">
              <a href="https://thewhitelab.org">thewhitelab.org</a>
            </span>
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
      <version :version="version"></version>
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
        <div class="columns">
          <div class="column card">
            <div class="card-content">
              <h3 class="title is-size-4">Hemolytic Prediction</h3>
              <h6 class="subtitle is-size-6">
                Predicted ability for peptide to kill red blood cells
              </h6>
              <tf-prediction
                url="https://raw.githubusercontent.com/ur-whitelab/peptide-dashboard/master/models/hemo-rnn/"
                :sequence="sequence"
              ></tf-prediction>
              <div class="ref-footer">
                <reference
                  reflink="https://pubs.acs.org/doi/10.1021/acs.jcim.0c00946"
                  reftitle="Investigating Active Learning and Meta-Learning for Iterative Peptide Design"
                  journal="J. Chem. Inf. Model."
                  year="2021"
                ></reference>
                <br />
                <reference
                  reflink="https://academic.oup.com/nar/article-abstract/44/D1/D1087/2503090"
                  reftitle="APD3: the antimicrobial peptide database as a tool for research and education."
                  journal="Nucleic acids research"
                  year="2016"
                ></reference>
              </div>
            </div>
          </div>
          <div class="card column">
            <div class="card-content">
              <h3 class="title is-size-4">Solubility Prediction</h3>
              <h6 class="subtitle is-size-6">
                Predicted solubility of given sequence
              </h6>
              <tf-prediction
                url="https://raw.githubusercontent.com/ur-whitelab/peptide-dashboard/master/models/sol-rnn/"
                :sequence="sequence"
              ></tf-prediction>
              <div class="ref-footer">
                <reference
                  reflink="https://pubs.acs.org/doi/10.1021/acs.jcim.0c00946"
                  reftitle="Investigating Active Learning and Meta-Learning for Iterative Peptide Design"
                  journal="J. Chem. Inf. Model."
                  year="2021"
                ></reference>
                <br />
                <reference
                  reflink="https://febs.onlinelibrary.wiley.com/doi/abs/10.1111/j.1742-4658.2012.08603.x"
                  reftitle="PROSO II–a new method for protein solubility prediction"
                  journal="The FEBS journal "
                  year="2012"
                ></reference>
              </div>
            </div>
          </div>
        </div>
        <div class="columns">
          <div class="card column">
            <div class="card-content">
              <h3 class="title is-size-4">Nonfouling Prediction</h3>
              <h6 class="subtitle is-size-6">
                Predicted ability to resist non-specific interactions
              </h6>
              <p class="card-header-subtitle is-size-5 is-spaced"></p>
              <tf-prediction
                url="https://raw.githubusercontent.com/ur-whitelab/peptide-dashboard/master/models/human-rnn/"
                :sequence="sequence"
              ></tf-prediction>
              <div class="ref-footer">
                <reference
                  reflink="https://onlinelibrary.wiley.com/doi/abs/10.1002/pep2.24079"
                  reftitle="Classifying antimicrobial and multifunctional peptides with Bayesian network models"
                  journal="Pep. Sci."
                  year="2018"
                ></reference>
                <br />
                <reference
                  reflink="https://doi.org/10.1039/C2SC21135A"
                  reftitle="Decoding nonspecific interactions from nature"
                  journal="Chem. Sci."
                  year="2012"
                ></reference>
              </div>
            </div>
          </div>
          <div class="card column">
            <header class="card-header">
              <h3 class="card-header-title is-size-4 is-spaced bd-anchor-title">
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
              <div class="ref-footer">
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
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section>
      <div class="container">
        <div class="columns">
          <div class="block column">
            <p>(c) Andrew White, 2022</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Version from "./Version.vue";
import SequenceViewer from "./SequenceViewer";
import Milton from "./results/Milton";
import SequenceInput from "./SequenceInput";
import TfPrediction from "./results/TfPrediction";
import Reference from "./Reference";
import pjson from "../../package.json";

export default {
  name: "App",
  components: {
    SequenceViewer,
    Milton,
    TfPrediction,
    SequenceInput,
    Reference,
    Version,
  },
  data() {
    return {
      sequence: "",
      viewWidth: 800,
      selectedIndex: -1,
      version: pjson["version"],
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

.column {
  margin: 1rem;
}
section {
  margin-bottom: 1.5em;
}

.tile {
  padding: 0.38rem;
}
.ref-footer {
  @media screen and (min-width: 1024px) {
    position: absolute;
    bottom: 0rem;
  }
  @media screen and (max-width: 1023px) {
    margin-top: 1rem;
    margin-bottom: 1rem;
  }
}
</style>
