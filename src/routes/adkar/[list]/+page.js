import { error } from '@sveltejs/kit';

import dikr_data from '$lib/data.json';

export function load({ params }) {
    const list_name = params.list;
    const dikr_list = dikr_data.find((list) => list.name === list_name);
    if (!dikr_list) error(404);

    return {
        adkar: dikr_list.adkar,
    };
}


export const ssr = false;
// export const prerender = true;
