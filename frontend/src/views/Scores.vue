<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <h1 class="text-h3 font-weight-bold mb-4">Scores</h1>
                <p class="text-body-1 mb-6">Track and analyze your disc golf performance</p>

                <!-- Placeholder for scores table -->
                <v-card>
                    <v-card-title>
                        Your Recent Scores
                        <v-spacer></v-spacer>
                        <v-text-field v-model="search" append-icon="mdi-magnify" label="Search" single-line
                            hide-details></v-text-field>
                    </v-card-title>
                    <v-data-table :headers="headers" :items="scores" :search="search" class="elevation-1">
                    </v-data-table>
                </v-card>
            </v-col>
            
            <v-col cols="12" class="mt-6">
                <v-btn color="primary" size="large">
                    <v-icon left>mdi-plus</v-icon>
                    Add New Score
                </v-btn>
            </v-col>
        </v-row>
        <!-- implement games into this table -->
        {{ gameIds }}
    </v-container>
</template>

<script setup>
import { ref } from 'vue';

// Sample data for the scores table
const search = ref('');
const headers = ref([
    { title: 'Date', key: 'date' },
    { title: 'Game', key: 'game' },
    { title: 'Score', key: 'score' },
]);

const scores = ref([
    { date: '2025-03-01 11:15', game: '1025', score: 540 },
    { date: '2025-02-25', game: '1025', score: 680 },
    { date: '2025-02-18', game: 'JYLY', score: 720 },
    { date: '2025-03-02', game: 'JYLY', score: 673 },
    { date: '2025-03-01 12:34', game: 'PP360', score: 540 },
    { date: '2025-02-01', game: 'PP360', score: 680 },
    { date: '2025-02-02', game: 'C1', score: 720 },
]);
const localGames = ref({ ...localStorage });
const gameIds = Object.keys(localGames.value);
</script>

<style scoped>
/* Add custom styles here */
</style>
