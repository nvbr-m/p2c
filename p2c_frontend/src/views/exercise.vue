<template>
<v-container fluid class="secondary">
    <v-row>
      <v-col>
        <v-card
          class="pa-2 mb-2 "
          outlined
          tile
        >
          <v-card-title > {{task.title}}</v-card-title>
          <v-card-text class="task">{{task.instruction}}</v-card-text>
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
        Pascal
          <prism-editor
      class="my-editor"
      readonly=True
      v-model="task.pascal_code"
      :highlight="highlighter_p"
      :line-numbers=lineNubers
    ></prism-editor>
        </v-card>
      </v-col>

      <v-col>
        <v-card
          outlined
          tile
        >
        C
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
        <v-icon large color=''> mdi-check-circle</v-icon>
        <div v-if="output.total" class="pa-2" style="color:white;
        font-weight: 600;">{{output.result}} {{output.passed}}/{{output.total}} </div>
        <v-btn
      depressed
      elevation="0"
      class="primary"
      text
      v-on:click="getOutput"
      >отправить
</v-btn>
    </v-row>
     <router-view></router-view>
  </v-container>
</template>

<script>
import axios from 'axios';
import { PrismEditor } from 'vue-prism-editor';
import 'vue-prism-editor/dist/prismeditor.min.css';
import { highlight, languages } from 'prismjs/components/prism-core';
import 'prismjs/components/prism-clike';
import 'prismjs/components/prism-c';
import 'prismjs/components/prism-pascal';
import 'prismjs/themes/prism-tomorrow.css';

const defualtCode = `#include <stdio.h>

int main (void)
{

  return 0;
}`;

export default {
  name: 'Exercise',
  components: {
    PrismEditor,
  },
  data: () => ({
    form: {
      code: defualtCode,
    },
    task: [],
    output: {
      total: '',
      resul: '',
    },
    lineNubers: true,
  }),
  created() {
    this.getDetail();
  },
  watch: {
    $route: 'getDetail',
  },
  methods: {
    getOutput() {
      axios.post(`http://127.0.0.1:8000/api/tasks/${this.$route.params.id}/`, this.form)
        .then((response) => {
          this.output = response.data;
        });
    },
    getDetail() {
      axios.get(`http://127.0.0.1:8000/api/tasks/${this.$route.params.id}`)
        .then((response) => {
          this.task = response.data;
          this.output = {
            total: '',
            resul: '',
          };
        });
    },
    highlighter(code) {
      return highlight(code, languages.c);
    },
    highlighter_p(code) {
      return highlight(code, languages.pascal);
    },
  },
};
</script>

<style >
.task {
  font-size: 18px;
}
.carde {
  background: #2d2d2d;
}
.my-editor {
  background: #2d2d2d;
  color: rgb(224, 224, 224);

  font-family: Fira code, Fira Mono, Consolas, Menlo, Courier, monospace;
  font-size: 14px;
  line-height: 1.5;
  padding: 5px;
  height: 500px;
  min-width: 300px;
  display: flex;
  decoration: none;

}

:active, :hover, :focus {
    outline: 0;
    outline-offset: 0;
}
</style>
