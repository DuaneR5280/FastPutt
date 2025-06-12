<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <h1 class="text-h3 font-weight-bold mb-4">Scores</h1>
                <p class="text-body-1 mb-6">Track and analyze your disc golf performance</p>
                <v-data-table
                    :headers="headers"
                    :items="gameData"
                    class="elevation-1"
                    item-key="uuid"
                    style="cursor:pointer"
                    @click:row="(_, row) => goToGame(row.item)"
                ></v-data-table>
            </v-col>
            <v-col cols="12" class="mt-6">
                <v-btn color="primary" size="large">
                    <v-icon left>mdi-plus</v-icon>
                    Add New Score
                </v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const headers = [
    { title: 'Date', key: 'date' },
    // { title: 'Game ID', key: 'uuid' },
    { title: 'Total Makes', key: 'totalMakes' },
    { title: 'Total Attempts', key: 'totalAttempts' },
    { title: 'Rules', key: 'gameRules' },
    { title: 'Duration', key: 'durationDisplay' }
];

const gameData = ref([]);

onMounted(async () => {
    try {
        const response = await fetch('/api/games');
        if (!response.ok) {
            throw new Error('Failed to fetch games');
        }
        const games = await response.json();
        gameData.value = games.map(game => ({
            ...game,
            date: formatDateOnly(game.gameStart),
            durationDisplay: formatDuration(game.gameDuration),
        }));
    } catch (err) {
        console.error('Error loading games:', err);
        gameData.value = [];
    }
});

function formatDateOnly(isoString) {
    if (!isoString) return '';
    const date = new Date(isoString);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

function formatDuration(seconds) {
    if (typeof seconds !== 'number' || isNaN(seconds)) return '';
    if (seconds < 60) {
        return `${Math.round(seconds)} s`;
    } else if (seconds < 3600) {
        return `${Math.floor(seconds / 60)} min`;
    } else {
        const hours = Math.floor(seconds / 3600);
        const minutes = Math.floor((seconds % 3600) / 60);
        return `${hours}h ${minutes}m`;
    }
}

function goToGame(item) {
    if (item && item.uuid) {
        router.push(`/games/${item.uuid}`);
    }
}
</script>

<style scoped>
/* Add custom styles here */
</style>
