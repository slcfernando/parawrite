<script lang="ts">
    let value = $state('');

    const gridCell = 'row-start-1 col-start-1';
    const textareaStyle = 'border-0 p-0 text-base leading-6 focus:ring-0 w-full text-wrap wrap-break-word';
</script>

<div class="text-center text-grandis-100 mb-24">
    <h1 class="font-satisfy text-8xl">Parawrite</h1>
    <p class="text-xl">Your personal writing companion</p>
</div>

<div class="flex justify-center">
    <div class="shadow-lg shadow-black bg-white w-[210mm] min-h-[297mm] p-6 sm:p-12 lg:p-24 text-black grid grid-cols-1">
        <div class="invisible whitespace-pre-wrap {gridCell} {textareaStyle}" aria-hidden="true">{value}</div>
        <textarea placeholder="Enter your text here" class="resize-none overflow-hidden {gridCell} {textareaStyle}" bind:value></textarea>
    </div>
</div>
