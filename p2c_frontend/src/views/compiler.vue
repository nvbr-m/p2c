<template>
<v-container fluid class="secondary">
    <v-row class="pt-8">
      <v-col
      >
        <v-card
          outlined
          tile
        >
          Code
          <prism-editor
      class="my-editor"
      :highlight="highlighter"
      :line-numbers=lineNubers
      v-model="form.code"
    ></prism-editor>
        </v-card>
      </v-col>

      <v-col>
        <v-card
          outlined
          tile
        >
          Output
          <prism-editor
      class="my-editor"
      readonly=True
      :highlight="highlighter"
      v-model="output.result"
    ></prism-editor>
        </v-card>
      </v-col>
    </v-row>
      <v-spacer></v-spacer>
      <v-row>
        <v-textarea class="pa-4"
          filled
          label="Input"
          rows="4"
          no-resize
          v-model="form.input"
          row-height="30"></v-textarea>
      </v-row>
      <v-spacer></v-spacer>
    <v-row class="pa-4" align="right" justify="space-around" >
        <v-icon large> mdi-clock </v-icon>
        <div class="pa-2" style="color:white;">{{output.time}} s</div>
        <v-icon large> mdi-view-stream </v-icon>
        <div class="pa-2" style="color:white;">{{output.memory}} kb</div>
        <v-btn
      depressed
      elevation="0"
      class="primary"
      text
      v-on:click="getOutput"
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

const defualtCode = `#include <stdio.h>

int main (void)
{
  printf("Hello World");
  return 0;
}`;

export default {
  name: 'Compiler',
  components: {
    PrismEditor,
  },
  data: () => ({
    form: {
      code: defualtCode,
      input: '',
    },
    output: {
      memory: '0.00',
      time: '0.00',
      result: '',
    },
    lineNubers: true,
  }),
  methods: {
    getOutput() {
      axios.post('http://localhost:8000/api/compiler/', this.form)
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
  height: 600px;
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
