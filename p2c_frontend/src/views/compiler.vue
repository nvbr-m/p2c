<template>
<v-container fluid class="primary">
    <v-row>
      <v-col>
        <v-card
          class="pa-2 mb-2 "
          outlined
          tile
        >
          <v-card-title>Hello, World!</v-card-title>
          <v-card-text >Выведите в консоль фразу "Hello, World!2"</v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col
      >
        <v-card
          outlined
          tile
        >
          <prism-editor
      class="my-editor"
      :highlight="highlighter"
      :line-numbers=lineNubers
    ></prism-editor>
        </v-card>
      </v-col>

      <v-col>
        <v-card
          outlined
          tile
        >
          <prism-editor
      class="my-editor"
      v-model="form.code"
      :highlight="highlighter"
      :line-numbers=lineNubers
    ></prism-editor>
        </v-card>
      </v-col>
    </v-row>

      <v-spacer></v-spacer>
    <v-row class="pa-4" align="right" justify="space-around" >
        <v-icon large> mdi-clock </v-icon>
        <div class="pa-2" style="color:white;">0.0 с</div>
        <v-icon large> mdi-view-stream </v-icon>
        <div class="pa-2" style="color:white;">0.0 с</div>
        <v-icon large> mdi-check-circle</v-icon>
        <div class="pa-2" style="color:white;">0.0 с</div>
        <v-btn
      depressed
      elevation="0"
      flat
      class="secondary"
      text
      >Пропустить
</v-btn>
        <v-btn
      depressed
      elevation="0"
      class="primary"
      text
      >отправить
</v-btn>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';
import { PrismEditor } from 'vue-prism-editor';
import 'vue-prism-editor/dist/prismeditor.min.css';
import { highlight, languages } from 'prismjs/components/prism-core';
import 'prismjs/components/prism-clike';
import 'prismjs/components/prism-c';
import 'prismjs/themes/prism-tomorrow.css';

export default {
  name: 'Compiler',
  components: {
    PrismEditor,
  },
  data: () => ({
    form: {
      chk: '1',
      code: '123',
      inp: null,
    },
    output: '',
    lineNubers: true,
  }),
  methods: {
    getOutput() {
      axios.post('http://localhost:8000/wow/', this.form)
        .then((response) => {
          this.output = response.data;
        });
    },
    highlighter(code) {
      return highlight(code, languages.c);
    },
  },
};
</script>

<style lang="scss" scoped>
// required class
.my-editor {
  background: #2d2d2d;
  color: #ccc;

  font-family: Fira code, Fira Mono, Consolas, Menlo, Courier, monospace;
  font-size: 14px;
  line-height: 1.5;
  padding: 5px;
  height: 500px;
  min-width: 300px;
  display: flex;

}

// optional
.prism-editor__textarea:focus {
  outline: 0;
}

// not required:
.output {
  background: #2d2d2d;
  color: #ccc;

  font-family: Fira code, Fira Mono, Consolas, Menlo, Courier, monospace;
  font-size: 14px;
  line-height: 1.5;
  padding: 5px;
  max-height: 500px;
  min-height: 200px;
  width: 500px;
  resize: none;

}

</style>
