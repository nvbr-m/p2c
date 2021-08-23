<template>
<v-container fluid class="secondary">
    <v-row>
      <v-col>
        <v-card
          class="pa-2 mb-2 "
          outlined
          tile
        >
          <v-card-title > Hello, World!</v-card-title>
          <v-card-text class="task">Выведите в консоль строку "Hello, World!"</v-card-text>
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
      v-model="form.pascal"
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
        <div class="pa-2 icons" style="color:white; font-weight: 600;">0.0 с</div>
        <v-icon large> mdi-view-stream </v-icon>
        <div class="pa-2" style="color:white; font-weight: 600;">1376 kb</div>
        <v-icon large> mdi-check-circle</v-icon>
        <div class="pa-2" style="color:white; font-weight: 600;">1/1 </div>
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
import 'prismjs/themes/prism.css';

export default {
  name: 'Exercise',
  components: {
    PrismEditor,
  },
  data: () => ({
    form: {
      chk: '1',
      code: '123',
      inp: null,
      pascal: '',
    },
    output: '',
    lineNubers: true,
    id: 0,
  }),
  created: () => {
    console.log(this.$route.params.id);
  },
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
  color: rgb(0, 0, 0);

  font-family: Fira code, Fira Mono, Consolas, Menlo, Courier, monospace;
  font-size: 14px;
  line-height: 1.5;
  padding: 5px;
  height: 500px;
  min-width: 300px;
  display: flex;

}
</style>
