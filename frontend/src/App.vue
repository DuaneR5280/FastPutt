<template>
    <v-app>
        <v-navigation-drawer v-model="drawer" app>
            <v-list>
                <v-list-item v-for="(item, i) in menuItems" :key="i" :to="item.path" :prepend-icon="item.icon"
                    :title="item.title"></v-list-item>
            </v-list>
        </v-navigation-drawer>

        <v-app-bar app>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-app-bar-title>FastPutt Disc Golf</v-app-bar-title>
        </v-app-bar>

        <v-main>
            <v-container fluid>
                <router-view></router-view>
            </v-container>
        </v-main>

        <v-footer app>
            <div>&copy; {{ new Date().getFullYear() }} - FastPutt Disc Golf</div>
        </v-footer>
    </v-app>
</template>

<script setup>
import { ref } from 'vue';

const drawer = ref(false);
const menuItems = ref([
    { title: 'Home', path: '/', icon: 'mdi-home' },
    { title: 'Scores', path: '/scores', icon: 'mdi-scoreboard' },
    { title: 'Courses', path: '/courses', icon: 'mdi-map' }
]);
</script>

<style>
/* Global styles can go here */
</style>
