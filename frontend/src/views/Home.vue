<template>
<v-container>
    <v-row class="text-center">
    <v-col cols="12">
        <h1 class="text-h3 font-weight-bold mb-4">Welcome to FastPutt</h1>
        <p class="text-h6 mb-6">Your disc golf score tracking application</p>
        <v-img
        src="https://via.placeholder.com/800x400?text=Disc+Golf+Hero+Image"
        height="400"
        class="rounded-lg"
        ></v-img>
    </v-col>
    <v-col cols="12" class="mt-6">
        <v-row>
        <v-col cols="12" md="6">
            <v-card elevation="2" class="pa-4">
            <v-card-title class="text-h5">Track Your Scores</v-card-title>
            <v-card-text>
                Record your scores for every round and track your progress over time!
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" to="/scores">View Scores</v-btn>
            </v-card-actions>
            </v-card>
        </v-col>
        <v-col cols="12" md="6">
            <v-card elevation="2" class="pa-4">
            <v-card-title class="text-h5">Explore Courses</v-card-title>
            <v-card-text>
                Browse our database of disc golf courses and find your next challenge.
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" to="/courses">View Courses</v-btn>
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

