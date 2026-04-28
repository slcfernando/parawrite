<script lang="ts">
    import favicon from '$lib/assets/favicon.svg';

    import './layout.css';

    let { children } = $props();
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>

<main class="min-h-screen bg-mandalay-900 p-24 font-lora">
    {@render children()}
</main>
