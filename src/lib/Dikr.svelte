<script>
    let {value, count, i, removeFn} = $props();
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

<button class="block m-auto w-full rounded-md bg-green-400 text-white mt-5 pt-1" onclick={count_current -= 1}>
    <p>{value}</p>
    <hr />
    <p dir="rtl" class="flex justify-around w-3/4 mx-auto">
        <span>{count_current}</span> 
        <span>|</span>
        <span>{count}</span>
    </p>
</button>
