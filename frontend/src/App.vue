<template>
    <v-app>
        <v-navigation-drawer v-model="drawer" app>
            <v-list>
                <v-list-item v-for="(item, i) in menuItems" :key="i" :to="item.path" :prepend-icon="item.icon"
                    :title="item.title"></v-list-item>
            </v-list>
            <v-divider></v-divider>
            <v-list>
                <v-list-item>
                    <v-switch v-model="darkMode" :prepend-icon="darkMode ? 'mdi-weather-night' : 'mdi-weather-sunny'"
                        :label="darkMode ? 'Dark Mode' : 'Light Mode'"></v-switch>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>

        <v-app-bar app>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-app-bar-title>FastPutt</v-app-bar-title>
        </v-app-bar>

        <v-main>
            <v-container fluid>
                <router-view></router-view>
            </v-container>
        </v-main>
        <!-- Footer 
        <v-footer app>
            <div>&copy; {{ new Date().getFullYear() }} - FastPutt Disc Golf</div>
        </v-footer>
        -->
    </v-app>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useTheme } from 'vuetify';

const theme = useTheme();
const darkMode = ref(theme.global.name.value === 'dark');

watch(darkMode, (newValue) => {
    theme.global.name.value = newValue ? 'dark' : 'light';
});

const drawer = ref(false);
const menuItems = ref([
    { title: 'Home', path: '/', icon: 'mdi-home' },
    // { title: 'Sessions', path: '/sessions', icon: 'mdi-scoreboard' },
    { title: 'Games', path: '/games', icon: 'mdi-gamepad' },
    // { title: 'Stats', path: '/stats', icon: 'mdi-chart-bar' },
    // { title: 'Leagues', path: '/leagues', icon: 'mdi-account-group' },
    // { title: 'Settings', path: '/settings', icon: 'mdi-cog' },
]);
</script>

<style>
/* Global styles can go here */
</style>
