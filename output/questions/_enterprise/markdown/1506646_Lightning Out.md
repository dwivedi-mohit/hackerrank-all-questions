# Lightning Out

## Metadata

- **ID:** 1506646
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Lightning Out, Lightning Component, Hard, Lightning

## Summary

This multiple choice question evaluates Lightning components, VisualForce integration, and JavaScript callback handling concepts, ideal for senior-level roles. The problem requires predicting the outcome of a button click in a Lightning component that interacts with a VisualForce page.

## Problem Statement

What will be the result of previewing this VisualForce page and hitting the Fire button?

 

SampleComponent.cmp

`<aura:component implements="flexipage:availableForAllPageTypes,force:appHostable" access="global">
    <!--Declare Attributes-->
    <aura:attribute name="vfMessageMethod" type="object" description="This attribute is for visualforce page javascript method"/>
     
    <!--Component Start-->
    <div class="slds-m-around_xx-large">
        <lightning:button variant="Brand" class="slds-button" label="Fire" onclick="{!c.doAction}"/>
    </div>
    <!--Component End-->
</aura:component>`
```

 

SampleComponentController.js 

`({
    doAction : function(component, event, helper) {
        var msg = 'Welcome to HackerRank';
        var messagMethod = component.get("v.vfMessageMethod");
        messagMethod(msg, function(){
            //handle callback
        });
        var toastEvent = $A.get("e.force:showToast");
          toastEvent.setParams({
            "title": "Success!",
            "message": "The message will be displayed here."
          });
          toastEvent.fire();
    }
})`
```

 

SampleApp.app

`<aura:application extends="ltng:outApp" access="global">
    <!--Lightning component-->
    <aura:dependency resource="c:SampleComponent"/>
    <aura:dependency resource="markup://force:showToast" type="EVENT"/>
</aura:application>`
```

 

Sample.vfp

`<apex:page sidebar="false" showHeader="false">
    <apex:includeLightning />
    <!--Lightning Container-->
    <div style="width:100%;height:100px;" id="LightningContainer"/>
     
    <script type="text/javascript">
    //Create Lightning Component
    $Lightning.use("c:SampleApp", function() {
        $Lightning.createComponent("c:SampleComponent", { 
            vfMessageMethod : getMessage, //Method to call from lightning component
        },"LightningContainer", function(component) {
            console.log('Component created');
        });
    });
     
    //Function to call from Lightning Component
    function getMessage(welcomeMsg){
        alert(welcomeMsg);
    }
    </script>
</apex:page>`
```

## Preview

What will be the result of previewing this VisualForce page and hitting the Fire
