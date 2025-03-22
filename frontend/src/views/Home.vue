<template>
<v-container>
    <v-row class="text-center">
    <v-col cols="12">
        <img :src="require('../assets/fastputtUFO2.webp')" alt="FastPutt Logo" width="300" class="mb-4" />
        <h1 class="text-h3 font-weight-bold mb-4">FastPutt</h1>
        <h2></h2>
        <p class="text-h6 mb-6">Disc golf putting application</p>
    </v-col>
    <v-col cols="12" class="mt-6">
        <v-row>
        <v-col cols="12" md="6">
            <v-card elevation="2" class="pa-4">
            <v-card-title class="text-h5">Track Your Scores</v-card-title>
            <v-card-text>
                Record your scores for every session and track your progress with stats over time!
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" to="/scores">View Scores</v-btn>
            </v-card-actions>
            </v-card>
        </v-col>
        <v-col cols="12" md="6">
            <v-card elevation="2" class="pa-4">
            <v-card-title class="text-h5">Games</v-card-title>
            <v-card-text>
                Pick a game from the list, JYLY, Ladders, and more. Start improving your putting today!
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" to="/games">View Games</v-btn>
            </v-card-actions>
            </v-card>
        </v-col>
        </v-row>
    </v-col>
    </v-row>
</v-container>
</template>

<script setup>
// Home page component
</script>

<style scoped>
/* Add custom styles here */
</style>

