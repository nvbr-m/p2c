import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import colors from 'vuetify/lib/util/colors';

Vue.use(Vuetify);

const opts = {
  icons: { iconfont: 'mdi' },
  theme: {
    dark: true,
    themes: {
      light: {
        primary: colors.blue, // #E53935
        secondary: colors.blue, // #FFCDD2
        accent: colors.indigo.base, // #3F51B5
        background: colors.red.darken1,
      },
      dark: {
        primary: '#1976D2',
        secondary: '#424242',
        accent: '#82B1FF',
        error: '#FF5252',
        info: '#2196F3',
        success: '#4CAF50',
        warning: '#FFC107',
        background: colors.grey.darken3,
      },
    },
  },
};

export default new Vuetify(opts);
