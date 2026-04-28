<script lang="ts">
    import favicon from '$lib/assets/favicon.svg';

    import './layout.css';

    let { children } = $props();
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>

<main class="bg-mandalay-900 p-24 min-h-screen font-lora">
    {@render children()}
</main>
