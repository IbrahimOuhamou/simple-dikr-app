<script>
    let {value, count, virtue = null, i, removeFn} = $props();
    let count_current = $state(count);

    // function decrement() {
    //     count_current -= 1;
    //     if(count_current <= 0) {
    //         removeFn(i);
    //     }
    // }

    $effect(() => {
        if(count_current <= 0) {
            removeFn(i);
        }
    })
</script>

<button class="block m-auto w-full rounded-md bg-green-500 text-white text-lg mt-5 pt-1" onclick={() => {count_current -= 1}}>
    <p class="p-4">{value}</p>
    <hr />
    {#if virtue}
        <p dir="rtl" class="font-thin text-sm">{virtue}</p>
        <hr />
    {/if}
    <p dir="rtl" class="flex justify-around w-3/4 mx-auto">
        <span>{count_current}</span> 
        <span>|</span>
        <span>{count}</span>
    </p>
</button>
