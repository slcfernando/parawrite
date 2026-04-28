<script lang="ts">
    let value = $state('');

    const gridCell = 'row-start-1 col-start-1';
    const textareaStyle =
        'border-0 p-0 text-base leading-6 focus:ring-0 w-full text-wrap wrap-break-word';
</script>

<div class="mb-24 text-center text-grandis-100">
    <h1 class="font-satisfy text-6xl sm:text-8xl">Parawrite</h1>
    <p class="text-base sm:text-xl">Your personal writing companion</p>
</div>

<div class="flex justify-center">
    <div
        class="grid min-h-[297mm] w-[210mm] grid-cols-1 bg-white p-6 text-black shadow-lg shadow-black sm:p-12 lg:p-24"
    >
        <div class="invisible whitespace-pre-wrap {gridCell} {textareaStyle}" aria-hidden="true">
            {value}
        </div>
        <textarea
            placeholder="Enter your text here"
            class="resize-none overflow-hidden {gridCell} {textareaStyle}"
            bind:value
        ></textarea>
    </div>
</div>
