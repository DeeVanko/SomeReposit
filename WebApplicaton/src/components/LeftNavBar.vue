<template>
    <aside class="NAVBAR">
        <NavigationSystem1/>
        <NavigationSystem2/>
        <NavigationSystem3/>
        <NavigationSystem4/>
        <NavigationSystem5/>
        <NavigationSystem6/>
        <div class="flex"></div>
        <NavigationSystem7/>
        <NavigationSystemSettings/>
        <NavigationSystemUser/>
    </aside>
</template>

<script>
import NavigationSystemSettings from '@/NavigationSystemComponents/NavigationSystem-Settings.vue';
import NavigationSystemUser from '@/NavigationSystemComponents/NavigationSystem-User.vue';
import NavigationSystem1 from '@/NavigationSystemComponents/NavigationSystem-1.vue';
import NavigationSystem2 from '@/NavigationSystemComponents/NavigationSystem-2.vue';
import NavigationSystem3 from '@/NavigationSystemComponents/NavigationSystem-3.vue';
import NavigationSystem4 from '@/NavigationSystemComponents/NavigationSystem-4.vue';
import NavigationSystem5 from '@/NavigationSystemComponents/NavigationSystem-5.vue';
import NavigationSystem6 from '@/NavigationSystemComponents/NavigationSystem-6.vue';
import NavigationSystem7 from '@/NavigationSystemComponents/NavigationSystem-7.vue';
export default {
  components: {
    NavigationSystemSettings,
    NavigationSystemUser,
    NavigationSystem1, NavigationSystem2, NavigationSystem3, NavigationSystem4, NavigationSystem5, NavigationSystem6, NavigationSystem7
  }
};
</script>
<style>
/* Ваши стили компонента Vue */
.NAVBAR {
            display: flex;
            flex-direction: column;
            position: fixed;
            top: 0;
            left: 0;
            width: 100px;
            height: 100%;
            background: var(--SC-DARK-BROWN-WL-INTENSITY);
            z-index: 1;

            border-right-style: solid;
            border-right-color: var(--SC-WHITE);
            border-right-width: 2px;
            box-shadow: 0 0 1rem var(--SC-RED);
        }
        .LINE-ITEM {
            position: relative;
            text-align: center;
            z-index: 1;
        }

        .FIRST-LINE-ITEM{
            padding: 15px 20px 15px 20px;
        }
        .FIRST-LINE-ITEM, .SECOND-LINE-ITEM, .THIRD-LINE-ITEM {
            background: var(--SC-DARK-BROWN-WL-INTENSITY);;
            cursor: pointer;
        }

        .SECOND-LINE-ITEMS {
            position: absolute;
            top: 0;
            left: -600px;
            width: max-content;
            z-index: -1;
            transition: all 450ms ease-in;
        }
        .THIRD-LINE-ITEMS{
            position: absolute;
            top: 0;
            left: -600px;
            width: max-content;
            z-index: -1;
            transition: all 450ms ease-in;
            display: flex;   
            flex-direction: row;
        }
        .SECOND-LINE-ITEM {
            padding: 15px 0px 15px 0px;
            float: left;
            width: 100%;
            background: var(--SC-DARK-BROWN-WM-INTENSITY);
            border: 1px var(--SC-WHITE) solid;
            box-shadow: 0 0 0.5rem var(--SC-RED);
            margin-bottom: 2px;
        }
        .THIRD-LINE-ITEM {
            padding: 20px 35px;
            float: left;
            width: max-content;
            background: var(--SC-DARK-BROWN-WM-INTENSITY);
            border: 1px var(--SC-WHITE) solid;
            box-shadow: 0 0 0.5rem var(--SC-RED);
            margin-right: 2px;
        }
        .FIRST-LINE-ITEM:hover, .SECOND-LINE-ITEM:hover, .THIRD-LINE-ITEM:hover {
            background: var(--SC-ORANGE);
            border: 1px var(--SC-WHITE) solid;
        }
        .LINE-ITEM:hover .SECOND-LINE-ITEMS, .LINE-ITEM:hover .THIRD-LINE-ITEMS{
            left: 122px;
        }
        .NAVBAR span {
            display: block;
            text-transform: uppercase;
        }
        .Rout, .LINE-ITEM a{
            display: block;
            height: 100%;
            text-decoration: none;
            color: inherit;
        }
        .flex {
            flex: 1 1 0;
        }
        .NAVBAR .LINE-ITEM .FIRST-LINE-ITEM .material-symbols-outlined {
            text-shadow: var(--SC-RED) 0 0 0.9375rem;
            font-weight: 600;
            font-size: 2rem;
            color: var(--SC-RED);
        }
        .NAVBAR .LINE-ITEM .SECOND-LINE-ITEM .material-symbols-outlined {
            
            text-shadow: var(--SC-RED) 0 0 0.9375rem;
            font-weight: 600;
            font-size: 1.2rem;
            color: var(--SC-RED);
        }
        .NAVBAR .LINE-ITEM .THIRD-LINE-ITEM .material-symbols-outlined {
            text-shadow: var(--SC-RED) 0 0 0.9375rem;
            font-weight: 600;
            font-size: 1.2rem;
            color: var(--SC-RED);
        }
        .NAVBAR .LINE-ITEM .FIRST-LINE-ITEM .TAG {
            text-shadow: var(--SC-RED) 0 0 0.9375rem;
            font-weight: 800;
            font-size: 0.8rem;
            color: var(--SC-RED);
        }
        .NAVBAR .LINE-ITEM .SECOND-LINE-ITEM .TAG {
            text-shadow: var(--SC-RED) 0 0 0.9375rem;
            font-weight: 800;
            font-size: 0.8rem;
            color: var(--SC-RED);
        }
        .NAVBAR .LINE-ITEM .THIRD-LINE-ITEM .TAG {
            text-shadow: var(--SC-RED) 0 0 0.9375rem;
            font-weight: 800;
            font-size: 0.8rem;
            color: var(--SC-RED);
        }
/* Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');
</style>