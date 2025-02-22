<script>
	import dikr_data from '$lib/data.json';
</script>

{#each dikr_data as dikr_list}
	<a class="block mx-auto my-2 rounded-md text-white p-2 bg-green-400" href="/adkar/{dikr_list.name}">
		<p>{dikr_list.description}</p>
		<h3 class="text-xl">{dikr_list.name}</h3>
	</a>
{/each}
