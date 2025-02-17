<script>
    let {value, count, i, removeFn} = $props();
    let count_current = $state(count);

    function decrement() {
        count_current -= 1;
        if(count_current <= 0) {
            removeFn(i);
        }
    }
</script>

<div>
    <p>{value}</p>
    <button onclick={decrement}>{count_current}</button>
</div>

